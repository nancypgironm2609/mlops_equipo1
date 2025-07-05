# Importaciones directas para evitar problemas con importaciones relativas
import os
import sys

# Agregar el directorio actual al path
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from Calculadora import calculadora

# Importar el módulo Funciones
funciones_dir = os.path.join(current_dir, 'Funciones')
if funciones_dir not in sys.path:
    sys.path.insert(0, funciones_dir)

import Funciones

__all__ = ['calculadora', 'Funciones']
