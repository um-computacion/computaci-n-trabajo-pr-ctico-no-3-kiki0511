import unittest
from src.exceptions import ingrese_numero, NumeroDebeSerPositivo
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        # Caso en el que la entrada es un número positivo válido
        numero = ingrese_numero()
        self.assertEqual(numero, 100)