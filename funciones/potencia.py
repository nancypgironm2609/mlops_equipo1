def potencia(base, exponente):
    """
    Calcula la potencia de un número elevado a otro.

    Parámetros:
        base (float): La base de la potencia.
        exponente (float): El exponente al que se eleva la base.

    Retorna:
        float: El resultado de base ** exponente.
    """
    try:
        return base ** exponente
    except OverflowError:
        return "Resultado demasiado grande para representarse."
    except TypeError:
        return "Los valores deben ser números."
