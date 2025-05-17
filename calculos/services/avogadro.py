AVOGADRO = 6.022e23

def calcular_particulas(moles: float) -> float:
    return moles * AVOGADRO

def calcular_moles_desde_particulas(particulas: float) -> float:
    resultado = round(particulas / AVOGADRO, 2)
    return resultado