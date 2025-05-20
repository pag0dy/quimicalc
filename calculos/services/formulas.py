from pyvalem.formula import Formula
import periodictable as pt
from mendeleev import element

def calcular_formula_empirica(composicion_porcentual: dict):
    """
    Calcula la fórmula empírica a partir de la composición porcentual.

    Args:
        composicion_porcentual (dict): Un diccionario donde las claves son
                                       los símbolos de los elementos (ej. 'C', 'H', 'O')
                                       y los valores son sus porcentajes en masa.

    Returns:
        str: La fórmula empírica del compuesto.
    """
    moles = {}
    for elemento, porcentaje in composicion_porcentual.items():
        try:
            masa_atomica = element(elemento).atomic_weight
        except Exception:
            raise AttributeError(f"No se encontró la masa atómica para '{elemento}'. "
                  "Asegúrate de que el símbolo del elemento es correcto.")
        
        gramos = porcentaje
        moles[elemento] = gramos / masa_atomica

    min_moles = min(moles.values())

    proporcion_moles = {elem: m / min_moles for elem, m in moles.items()}

    multiplicador = 1
    while True:
        todos_enteros = True
        for valor in proporcion_moles.values():
            print(f"valor: {valor}")
            if abs(round(valor * multiplicador) - (valor * multiplicador)) > 0.01:
                todos_enteros = False
                break
        if todos_enteros:
            break
        multiplicador += 1
        if multiplicador > 10:
            raise ValueError("Advertencia: No se pudo encontrar una proporción entera simple. Intenta ajustar la tolerancia.")

    formula_empirica_dict = {
        elem: int(round(moles_ajustados * multiplicador))
        for elem, moles_ajustados in proporcion_moles.items()
    }
    return formula_empirica_dict


def calcular_formula_molecular(empirica_str: str, masa_molar_real: float) -> dict:
    """Función para calcular la fórmula molecular

    Args:
        empirica (dict): _description_
        masa_molar_real (float): _description_

    Returns:
        dict: _description_
    """
    atomos = Formula(empirica_str).atom_stoich
    masa_empirica = sum(getattr(pt, el).mass * cant for el, cant in atomos.items())
    factor = round(masa_molar_real / masa_empirica)
    return {el: cant * factor for el, cant in atomos.items()}

def parsear_composicion(composicion_str: str) -> dict[str, float]:
    """Parsea un string como 'C=40, H=6.71' a {'C': 40.0, 'H': 6.71}"""
    try:
        partes = composicion_str.split(",")
        elementos = {}
        for parte in partes:
            if "=" not in parte:
                continue
            simbolo, valor = parte.strip().split("=")
            elementos[simbolo.strip().capitalize()] = float(valor.strip())
        return elementos
    except Exception:
        raise ValueError("Formato inválido. Usa: C=40, H=6.71, O=53.29")
