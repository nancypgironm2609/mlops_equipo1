# Importaciones con múltiples estrategias para máxima compatibilidad
import os
import sys

# Estrategia 1: Importaciones relativas
try:
    from .Calculadora import calculadora
    from . import Funciones
except ImportError:
    # Estrategia 2: Importaciones absolutas
    try:
        from mlops_equipo1.Calculadora import calculadora
        from mlops_equipo1 import Funciones
    except ImportError:
        # Estrategia 3: Importaciones directas con path manipulation
        current_dir = os.path.dirname(__file__)
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        try:
            from Calculadora import calculadora
            import Funciones
        except ImportError:
            # Estrategia 4: Importar directamente desde archivos
            import importlib.util
            
            calculadora_path = os.path.join(os.path.dirname(__file__), 'Calculadora.py')
            
            # Cargar Calculadora
            spec = importlib.util.spec_from_file_location("Calculadora", calculadora_path)
            calc_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(calc_module)
            calculadora = calc_module.calculadora
            
            # Para Funciones, intentar importar como módulo
            funciones_dir = os.path.join(current_dir, 'Funciones')
            if funciones_dir not in sys.path:
                sys.path.insert(0, funciones_dir)
            import Funciones

__all__ = ['calculadora', 'Funciones']
