import periodictable as pt
from pyvalem.formula import Formula

def calcular_masa_molar(formula_str: str) -> float:
    """Función para calcular masa molar

    Args:
        formula_str (str): Fórmula como string

    Returns:
        float: masa molar total
    """
    formula = Formula(formula_str)
    masa_total = 0
    for el, cant in formula.atom_stoich.items():
        masa_total += getattr(pt, el).mass * cant
    return masa_total
