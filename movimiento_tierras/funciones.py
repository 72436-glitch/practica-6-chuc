import math

# ================================
# VALIDACIÓN DE DATOS
# ================================
def validar(valor):
    if valor <= 0:
        raise ValueError("Todos los valores deben ser mayores que cero.")
    return valor


# ================================
# FUNCIONES DE CÁLCULO
# ================================

def volumen_losa(largo, ancho, espesor):
    """
    Calcula el volumen de una losa de concreto.
    Fórmula: V = largo * ancho * espesor
    """
    return validar(largo) * validar(ancho) * validar(espesor)


def volumen_zapata(largo, ancho, espesor):
    """
    Calcula el volumen de una zapata prismática.
    """
    return validar(largo) * validar(ancho) * validar(espesor)


def volumen_columna_rect(lado1, lado2, altura):
    """
    Calcula el volumen de una columna rectangular.
    """
    return validar(lado1) * validar(lado2) * validar(altura)


def volumen_columna_circ(diametro, altura):
    """
    Calcula el volumen de una columna circular.
    Fórmula: V = π * r² * h
    """
    radio = validar(diametro) / 2
    return math.pi * (radio ** 2) * validar(altura)


# ================================
# PRUEBAS INTERNAS
# ================================
def pruebas():
    assert round(volumen_losa(5, 4, 0.15), 2) == 3.00
    assert volumen_zapata(2, 2, 0.5) == 2.0
    assert volumen_columna_rect(0.3, 0.3, 3) == 0.27
    assert round(volumen_columna_circ(0.4, 3), 4) == round(math.pi * (0.2**2) * 3, 4)
    print("✔ TODAS LAS PRUEBAS PASARON CORRECTAMENTE.")