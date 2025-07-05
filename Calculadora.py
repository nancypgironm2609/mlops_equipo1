# Importaciones con múltiples estrategias
import os
import sys
import math

# Estrategia 1: Importaciones relativas
try:
    from .Funciones.Potencia import potencia
    from .Funciones.RaizCuadrada import raiz_cuadrada
except ImportError:
    # Estrategia 2: Importaciones absolutas
    try:
        from mlops_equipo1.Funciones.Potencia import potencia
        from mlops_equipo1.Funciones.RaizCuadrada import raiz_cuadrada
    except ImportError:
        # Estrategia 3: Importaciones directas con path manipulation
        funciones_dir = os.path.join(os.path.dirname(__file__), 'Funciones')
        if funciones_dir not in sys.path:
            sys.path.insert(0, funciones_dir)
        try:
            from Potencia import potencia
            from RaizCuadrada import raiz_cuadrada
        except ImportError:
            # Estrategia 4: Buscar archivos de manera más robusta
            import importlib.util
            
            # Buscar archivos en posibles ubicaciones
            possible_dirs = [
                os.path.join(os.path.dirname(__file__), 'Funciones'),
                os.path.join(os.getcwd(), 'mlops_equipo1', 'Funciones'),
                os.path.join(os.getcwd(), 'Funciones'),
                os.path.join(os.path.dirname(__file__), '..', 'mlops_equipo1', 'Funciones'),
                # Agregar la ruta correcta para GitHub Actions
                os.path.join(os.getcwd(), 'mlops_equipo1', 'mlops_equipo1', 'Funciones'),
            ]
            
            # Debug: imprimir información sobre las rutas que se están buscando
            print(f"DEBUG - __file__: {__file__}")
            print(f"DEBUG - os.getcwd(): {os.getcwd()}")
            print(f"DEBUG - os.path.dirname(__file__): {os.path.dirname(__file__)}")
            print("DEBUG - Buscando en directorios:")
            for i, dir_path in enumerate(possible_dirs):
                exists = os.path.exists(dir_path)
                print(f"  {i+1}. {dir_path} -> {'EXISTE' if exists else 'NO EXISTE'}")
                if exists:
                    try:
                        files = os.listdir(dir_path)
                        print(f"     Archivos: {files}")
                    except:
                        print("     No se pudo listar el directorio")
            
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

def calculadora(a, b, opcion):
    opcion = opcion.strip().lower()  # ← limpia espacios y capitalización

    if opcion == "sumar":
        return a + b
    elif opcion == "restar":
        return a - b
    elif opcion == "multiplicar":
        return a * b
    elif opcion == "dividir":
        if b == 0:
            return "No se puede dividir por cero."
        else:
            return a / b
    elif opcion == "raiz_cuadrada":
        if a < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo."
        else:
            return raiz_cuadrada(a)
    elif opcion == "potencia":
        return potencia(a, b)
    elif opcion == "salir":
        return "Saliendo del programa."
    else:
        return "Opción no válida."


# =====================
# 👇 Código interactivo SOLO si se ejecuta directamente
# =====================
if __name__ == "__main__":
    print(calculadora(25, 0, "raiz_cuadrada") == 5)

    print("Bienvenido a la calculadora")
    print("Selecciona una operación:")
    print("Puedes realizar las siguientes operaciones: sumar, restar, multiplicar, dividir,raiz cuadrada o salir.")

    ejecutar = True

    while ejecutar:
        opciones = input("¿Quieres sumar, restar, multiplicar, dividir, raiz_cuadrada o salir?: ").strip()

        if opciones == "sumar":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(calculadora(a, b, opciones))

        elif opciones == "restar":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(calculadora(a, b, opciones))

        elif opciones == "multiplicar":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(calculadora(a, b, opciones))

        elif opciones == "dividir":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(calculadora(a, b, opciones))

        elif opciones == "raiz_cuadrada":
            a = float(input("Número: "))
            print(calculadora(a, 0, opciones))

        elif opciones == "potencia":
            a = float(input("Base: "))
            b = float(input("Exponente: "))
            print(calculadora(a, b, opciones))

        elif opciones == "salir":
            print("Saliendo del programa.")
            ejecutar = False

        else:
            print("Opción no válida. Por favor, elige una opción válida.")
