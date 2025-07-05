# calculadora_prueba.py

def calculadora(a, b, opcion):
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
    elif opcion == "potencia":
        return a ** b
    else:
        return "Opción no válida."
