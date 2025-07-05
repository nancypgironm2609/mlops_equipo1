# test_calculadora.py

from calculadora_prueba import calculadora

def test_sumar():
    assert calculadora(3, 2, "sumar") == 5

def test_restar():
    assert calculadora(5, 2, "restar") == 3

def test_multiplicar():
    assert calculadora(4, 3, "multiplicar") == 12

def test_dividir():
    assert calculadora(10, 2, "dividir") == 5

def test_dividir_por_cero():
    assert calculadora(10, 0, "dividir") == "No se puede dividir por cero."

def test_potencia():
    assert calculadora(2, 3, "potencia") == 8

def test_raiz_cuadrada():
    assert calculadora(25, 0, "raiz_cuadrada") == 5

def test_opcion_invalida():
    assert calculadora(3, 4, "desconocida") == "Opción no válida."
