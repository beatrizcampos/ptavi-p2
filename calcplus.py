#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija


def operaciones(operadores, resultado, operacion):
    for operando in operadores[1:]:
        operando = int(operando)
        if operacion == "suma":
            resultado = calculadora.suma(resultado, operando)
        elif operacion == "resta":
            resultado = calculadora.resta(resultado, operando)
        elif operacion == "multiplica":
            resultado = calculadora.multiplicar(resultado, operando)
        elif operacion == "divide":
            resultado = calculadora.dividir(resultado, operando)
        else:
            sys.exit('Sólo puede ser sumar,restar, multiplicar o dividir.')
    return resultado

if __name__ == "__main__":
    fich = open(sys.argv[1], 'r')
    lineas = fich.readlines()
    calculadora = calcoohija.CalculadoraHija()
    for linea in lineas:
        elementos = linea.split(',')
        #La operacion es el primer elemento
        operacion = elementos[0]
        #El resto de elementos son operadores
        operadores = elementos[1:]
        operadores[-1] = operadores[-1][:-1]
        #Hacemos que resultado sea el primer elemento y "operando" el resto
        resultado = int(operadores[0])
        resultado = operaciones(operadores, resultado, operacion)
        print(resultado)
