"""Gerado por ProjExt

Exemplo de teste unitário"""

import os
import sys
import unittest
from math import pi

# Caminho relativo para pasta tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import area_circulo


class TestaAreaCirculo(unittest.TestCase):
    def teste_area(self):
        """Teste area quando raio >= 0"""
        self.assertAlmostEqual(area_circulo(1), pi)
        self.assertAlmostEqual(area_circulo(0), 0)
        self.assertAlmostEqual(area_circulo(2.1), pi * 2.1 ** 2)

    def teste_valores(self):
        """Testa os valores negativos"""
        self.assertRaises(ValueError, area_circulo, -2)

    def teste_tipos(self):
        """Testa os tipos"""
        self.assertRaises(TypeError, area_circulo, 3 + 5j)
        self.assertRaises(TypeError, area_circulo, True)
        self.assertRaises(TypeError, area_circulo, "Nome")
