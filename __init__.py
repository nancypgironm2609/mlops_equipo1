try:
    from .Calculadora import calculadora
    from . import Funciones
except ImportError:
    from mlops_equipo1.Calculadora import calculadora
    from mlops_equipo1 import Funciones

__all__ = ['calculadora', 'Funciones']
