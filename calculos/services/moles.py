CONVERSIONES_MASA = {
    "ug": 1e-6,
    "mg": 1e-3,
    "g": 1,
    "kg": 1e3,
    "ton": 1e6,
}

def convertir_a_gramos(valor: float, unidad: str) -> float:
    return valor * CONVERSIONES_MASA[unidad]

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
