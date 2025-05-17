def formatear_exponente(n: float, decimales: int = 2) -> str:
    """Convierte un número en notación científica estilo químico"""
    if n == 0:
        return "0"
    exponent = int(f"{n:e}".split("e")[1])
    base = n / (10 ** exponent)
    base_str = f"{base:.{decimales}f}"
    return f"{base_str} × 10<sup>{exponent}</sup>"

CONVERSIONES_MASA = {
    "ug": 1e-6,
    "mg": 1e-3,
    "g": 1,
    "kg": 1e3,
    "ton": 1e6,
}

def convertir_a_gramos(valor: float, unidad: str) -> float:
    return valor * CONVERSIONES_MASA[unidad]