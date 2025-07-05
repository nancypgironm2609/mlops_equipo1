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
            # Estrategia 4: Buscar archivos de manera más robusta
            import importlib.util
            
            # Buscar Calculadora.py en posibles ubicaciones
            possible_dirs = [
                os.path.dirname(__file__),
                os.path.join(os.getcwd(), 'mlops_equipo1'),
                os.getcwd(),
                # Ruta para estructura duplicada (GitHub Actions)
                os.path.join(os.getcwd(), 'mlops_equipo1', 'mlops_equipo1'),
                # Rutas relativas hacia arriba y luego hacia abajo
                os.path.join(os.path.dirname(__file__), '..', 'mlops_equipo1'),
                os.path.join(os.path.dirname(__file__), '..', '..', 'mlops_equipo1'),
                os.path.join(os.path.dirname(__file__), '..', '..', 'mlops_equipo1', 'mlops_equipo1'),
            ]
            
            calculadora_path = None
            
            for dir_path in possible_dirs:
                if os.path.exists(dir_path):
                    calc_candidate = os.path.join(dir_path, 'Calculadora.py')
                    if os.path.exists(calc_candidate):
                        calculadora_path = calc_candidate
                        break
            
            if calculadora_path:
                # Cargar Calculadora
                spec = importlib.util.spec_from_file_location("Calculadora", calculadora_path)
                calc_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(calc_module)
                calculadora = calc_module.calculadora
                
                # Para Funciones, intentar importar como módulo
                funciones_dir = os.path.join(os.path.dirname(calculadora_path), 'Funciones')
                if funciones_dir not in sys.path:
                    sys.path.insert(0, funciones_dir)
                import Funciones
            else:
                raise ImportError("No se pudo encontrar Calculadora.py")

__all__ = ['calculadora', 'Funciones']
