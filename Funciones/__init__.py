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
            # Estrategia 4: Buscar archivos de manera más robusta
            import importlib.util
            import glob
            
            # Buscar archivos Potencia.py y RaizCuadrada.py en posibles ubicaciones
            possible_dirs = [
                os.path.dirname(__file__),
                os.path.join(os.getcwd(), 'mlops_equipo1', 'Funciones'),
                os.path.join(os.getcwd(), 'Funciones'),
                # Ruta para estructura duplicada (GitHub Actions)
                os.path.join(os.getcwd(), 'mlops_equipo1', 'mlops_equipo1', 'Funciones'),
                # Rutas relativas hacia arriba y luego hacia abajo
                os.path.join(os.path.dirname(__file__), '..', 'mlops_equipo1', 'Funciones'),
                os.path.join(os.path.dirname(__file__), '..', '..', 'mlops_equipo1', 'Funciones'),
                os.path.join(os.path.dirname(__file__), '..', '..', 'mlops_equipo1', 'mlops_equipo1', 'Funciones'),
            ]
            
            potencia_path = None
            raiz_path = None
            
            for dir_path in possible_dirs:
                if os.path.exists(dir_path):
                    pot_candidate = os.path.join(dir_path, 'Potencia.py')
                    raiz_candidate = os.path.join(dir_path, 'RaizCuadrada.py')
                    if os.path.exists(pot_candidate) and os.path.exists(raiz_candidate):
                        potencia_path = pot_candidate
                        raiz_path = raiz_candidate
                        break
            
            if potencia_path and raiz_path:
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
            else:
                raise ImportError("No se pudieron encontrar los archivos Potencia.py y RaizCuadrada.py")

__all__ = ['potencia', 'raiz_cuadrada']
