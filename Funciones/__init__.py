# Importaciones con múltiples estrategias
import os
import sys

# Estrategia 1: Importaciones relativas
try:
    from .Potencia import potencia
    from .RaizCuadrada import raiz_cuadrada
except ImportError:
    # Estrategia 2: Importaciones absolutas
    try:
        from mlops_equipo1.Funciones.Potencia import potencia
        from mlops_equipo1.Funciones.RaizCuadrada import raiz_cuadrada
    except ImportError:
        # Estrategia 3: Importaciones directas con path manipulation
        current_dir = os.path.dirname(__file__)
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        try:
            from Potencia import potencia
            from RaizCuadrada import raiz_cuadrada
        except ImportError:
            # Estrategia 4: Importar directamente desde archivos
            import importlib.util
            
            potencia_path = os.path.join(os.path.dirname(__file__), 'Potencia.py')
            raiz_path = os.path.join(os.path.dirname(__file__), 'RaizCuadrada.py')
            
            # Cargar Potencia
            spec = importlib.util.spec_from_file_location("Potencia", potencia_path)
            potencia_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(potencia_module)
            potencia = potencia_module.potencia
            
            # Cargar RaizCuadrada
            spec = importlib.util.spec_from_file_location("RaizCuadrada", raiz_path)
            raiz_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(raiz_module)
            raiz_cuadrada = raiz_module.raiz_cuadrada

__all__ = ['potencia', 'raiz_cuadrada']
