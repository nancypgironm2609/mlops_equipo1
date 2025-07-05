# Importaciones directas de funciones desde los módulos
import os
import sys

# Agregar el directorio actual al path si no está
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Importar las funciones directamente
from Potencia import potencia
from RaizCuadrada import raiz_cuadrada

__all__ = ['potencia', 'raiz_cuadrada']
