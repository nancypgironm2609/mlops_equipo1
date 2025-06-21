
#
def calculadora(a,b,opcion):
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
    else:
        return "Opción no válida."
    
# Programa principal
print("Bienvenido a la calculadora")
print("Puedes realizar las siguientes operaciones: sumar, restar, multiplicar, dividir o salir.")
ejecutar= True

while ejecutar == True:
    opciones=input("quieres sumar restar multiplicar o dividir o salir?")
    if opciones == "sumar":
        a:float = float(input("primer numero: "))
        b:float = float(input("segundo numero: "))
        print(calculadora(a, b, opciones))
    elif opciones == "restar":
        a:float= float(input("primer numero: "))
        b:float = float(input("segundo numero: "))
        print(calculadora(a, b, opciones))
    elif opciones == "multiplicar":
        a:float = float(input("primer numero: "))
        b:float = float(input("segundo numero: "))
        print(calculadora(a, b, opciones))
    elif opciones == "dividir":
        a:float = float(input("primer numero: "))
        b :float= float(input("segundo numero: "))
        
        if b == 0:
            print("No se puede dividir por cero.")
        else:
            print(calculadora(a, b, opciones))
    elif opciones == "salir":
        print("Saliendo del programa.") 
        ejecutar= False
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
        
    
    