#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import sys
import calcoo
import calcoohija
import calcplus


if __name__ == "__main__":

    calculadora = calcoohija.CalculadoraHija()
    fichero = sys.argv[1]
    diccionario = {"suma": calculadora.suma,
                   "resta": calculadora.resta,
                   "multiplica": calculadora.multiplicar,
                   "divide": calculadora.dividir}
    with open(fichero, newline='') as fich:
        lineas = csv.reader(fich)
        for linea in lineas:
            resultado = calcplus.operaciones(linea, diccionario)
            print(resultado)
