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
            # Estrategia 4: Importar directamente desde archivos
            import importlib.util
            
            potencia_path = os.path.join(os.path.dirname(__file__), 'Funciones', 'Potencia.py')
            raiz_path = os.path.join(os.path.dirname(__file__), 'Funciones', 'RaizCuadrada.py')
            
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
