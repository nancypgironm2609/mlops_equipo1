from Funciones.RaizCuadrada import raiz_cuadrada
from Funciones.Potencia import potencia

import math

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
