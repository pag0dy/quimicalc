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

def calcular_formula_molecular(empirica: dict, masa_molar_real: float) -> dict:
    """Función para calcular la fórmula molecular

    Args:
        empirica (dict): _description_
        masa_molar_real (float): _description_

    Returns:
        dict: _description_
    """
    masa_empirica = sum(getattr(pt, el).mass * cant for el, cant in empirica.items())
    factor = round(masa_molar_real / masa_empirica)
    return {el: cant * factor for el, cant in empirica.items()}
