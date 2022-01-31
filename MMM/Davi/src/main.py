"""Gerado por ProjExt

Exemplo de um simples programa"""
from math import pi


def area_circulo(raio):
    if type(raio) not in [int, float]:
        raise TypeError("O Raio deve ser um número real não negativo")

    if raio < 0:
        raise ValueError("O Raio não pode ser negativo")
    return pi * (raio ** 2)
