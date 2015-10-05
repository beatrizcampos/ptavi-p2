#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija


def operaciones(operadores, resultado, operacion, diccionario):
    try:
        operar = diccionario[operacion]
    except KeyError:
        sys.exit('Sólo puede ser suma,resta, multiplica o divide.')
    for operando in operadores[1:]:
        operando = int(operando)
        resultado = operar(resultado, operando)
    return resultado

if __name__ == "__main__":
    fich = open(sys.argv[1], 'r')
    lineas = fich.readlines()
    calculadora = calcoohija.CalculadoraHija()
    diccionario = {"suma": calculadora.suma, "resta": calculadora.resta, "multiplica": calculadora.multiplicar, "divide": calculadora.dividir}
    for linea in lineas:
        elementos = linea.split(',')
        #La operacion es el primer elemento
        operacion = elementos[0]
        #El resto de elementos son operadores
        operadores = elementos[1:]
        operadores[-1] = operadores[-1][:-1]
        #Hacemos que resultado sea el primer elemento y "operando" el resto
        resultado = int(operadores[0])
        resultado = operaciones(operadores, resultado, operacion, diccionario)
        print(resultado)
