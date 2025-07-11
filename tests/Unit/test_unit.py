import sys
import os

# Agregar el directorio raíz del proyecto al path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from mlops_equipo1.Calculadora import calculadora
from mlops_equipo1.Funciones.RaizCuadrada import raiz_cuadrada
from mlops_equipo1.Funciones.Potencia import potencia


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

def test_opcion_invalida():
    assert calculadora(3, 4, "desconocida") == "Opción no válida."

def test_calculadora_raiz_cuadrada():
    assert calculadora(16, 0, "raiz_cuadrada") == 4.0

def test_calculadora_raiz_cuadrada_negativa():
    assert calculadora(-4, 0, "raiz_cuadrada") == "No se puede calcular la raíz cuadrada de un número negativo."
