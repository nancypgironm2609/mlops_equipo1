try:
    from .Potencia import potencia
    from .RaizCuadrada import raiz_cuadrada
except ImportError:
    from mlops_equipo1.Funciones.Potencia import potencia
    from mlops_equipo1.Funciones.RaizCuadrada import raiz_cuadrada

__all__ = ['potencia', 'raiz_cuadrada']
