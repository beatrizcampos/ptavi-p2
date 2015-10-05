#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import sys
import calcoo
import calcoohija


if __name__ == "__main__":

    calculadora = calcoohija.CalculadoraHija()
    fichero = sys.argv[1]

    with open(fichero, newline='') as fich:
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
            elif operacion == "resta":
                while j < len(operadores):
                    operando = int(operadores[j])
                    resultado = calculadora.resta(resultado, operando)
                    j = j + 1
            elif operacion == "multiplica":
                while j < len(operadores):
                    operando = int(operadores[j])
                    resultado = calculadora.multiplicar(resultado, operando)
                    j = j + 1
            elif operacion == "divide":
                while j < len(operadores):
                    operando = int(operadores[j])
                    resultado = calculadora.dividir(resultado, operando)
                    j = j + 1
            else:
                sys.exit('Sólo puede ser sumar,restar, multiplicar o dividir.')
            print(resultado)
            i = i + 1
