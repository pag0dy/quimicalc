def calcular_moles(masa: float, masa_molar: float) -> float:
    """Función para calcular número de moles (n)

    Args:
        masa (float): masa en gramos
        masa_molar (float): masa molar en gramos/mol

    Returns:
        float: moles (n)
    """
    return masa / masa_molar


def calcular_numero_particulas(moles: float) -> float:
    """Función para calcular número de partículas
    utilizando el número de Avogadro como const.

    Args:
        moles (float): moles (n)
        
    Returns:
        float: número de partículas
    """
    AVOGADRO = 6.022e23
    return moles * AVOGADRO
