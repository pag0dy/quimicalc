from pyvalem.formula import Formula
import periodictable as pt

def calcular_formula_empirica(masas: dict[str, float]) -> dict:
    """Función para calcular la fórmula empírica

    Args:
        masas (dict[str, float]): _description_

    Returns:
        dict: _description_
    """
    moles = {el: masa / getattr(pt, el).mass for el, masa in masas.items()}
    menor = min(moles.values())
    proporciones = {el: round(mol / menor) for el, mol in moles.items()}
    return proporciones

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
            elementos[simbolo.strip()] = float(valor.strip())
        return elementos
    except Exception:
        raise ValueError("Formato inválido. Usa: C=40, H=6.71, O=53.29")
