#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija


if __name__ == "__main__":
    fich = open(sys.argv[1], 'r')
    linea = fich.readlines()
    num_lineas = len(linea)  #numero de lineas que hay
    elementos = linea[0].split(',')  # elementos que hay en linea
    calculadora = calcoohija.CalculadoraHija()
    i = 0
    while i < num_lineas:  #Vamos cogiendo las lineas hasta llegar al final
       elementos = linea[i].split(',')
       operacion = elementos[0]#La operacion es el primer elemento
       operadores = elementos[1:]#El resto de elementos son operadores
       operadores[-1] = operadores[-1][:-1]
       #Hacemos que resultado sea el primer elemento y "operando" el resto
       resultado = int(operadores[0]) 
       j = 1
       if operacion == "suma":
           while j < len(operadores):
               operando = int(operadores[j]) 
               resultado = calculadora.suma(resultado, operando)
               j = j + 1
       if operacion == "resta":
           while j < len(operadores):
               operando = int(operadores[j]) 
               resultado = calculadora.resta(resultado, operando)
               j = j + 1
       if operacion == "multiplica":
           while j < len(operadores):
               operando = int(operadores[j]) 
               resultado = calculadora.multiplicar(resultado, operando)
               j = j + 1
       if operacion == "divide":
           while j < len(operadores):
               operando = int(operadores[j]) 
               resultado = calculadora.dividir(resultado, operando)
               j = j + 1
       print(resultado)
       i = i + 1
