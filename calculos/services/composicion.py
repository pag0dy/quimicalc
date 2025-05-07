import periodictable as pt
from pyvalem.formula import Formula

def calcular_composicion_porcentual(formula_str: str) -> dict:
    """Función para calcular composición porcentual

    Args:
        formula_str (str): Fórmula en string

    Returns:
        dict: Composición porcentual
    """
    formula = Formula(formula_str)
    atomos = formula.atom_stoich

    masa_total = sum(getattr(pt, el).mass * cant for el, cant in atomos.items())

    composicion = {
        el: round((getattr(pt, el).mass * cant / masa_total) * 100, 2)
        for el, cant in atomos.items()
    }

    return composicion
