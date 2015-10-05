#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import sys
import calcoo
import calcoohija


if __name__ == "__main__":

    calculadora = calcoohija.CalculadoraHija()
    fichero = sys.argv[1]
    with open(fichero, newline = '') as fich:
        lineas = csv.reader(fich)
        i = 0
        for linea in lineas:
            #La operacion es el primer elemento
            operacion = linea[0]
            #El resto de elementos son operadores
            operadores = linea[1:]
            #Hacemos que resultado sea el primer elemento y "operando" el resto
            resultado = int(operadores[0])
            j = 1
            if operacion == "suma":
                while j < len(operadores):
                    operando = int(operadores[j])
                    resultado = calculadora.suma(resultado, operando)
                    j = j + 1
            print(resultado)
            i = i + 1
 
