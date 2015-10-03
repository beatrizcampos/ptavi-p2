#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija


if __name__ == "__main__":
    fich = open(sys.argv[1],'r')
    linea = fich.readlines() 
    num_lineas = len(linea) ##numero de lineas que hay
    print('numero de lineas que hay en texto', num_lineas)
    elementos = linea[0].split(',')##elementos que hay en linea
    print('elementos', elementos) 
    print('numero de elementos', len(elementos)) ##numero elementos en linea
    print(elementos[0])  ## imprime el primer elemento
    print(elementos[1])  ##imprime el segundo elemento
    print(elementos[1:])

    calculadora = calcoohija.CalculadoraHija()
    i = 0
    while i < num_lineas:   #Vamos cogiendo las lineas hasta llegar al final
       elementos = linea[i].split(',')
       operacion = elementos[0] #La operacion es el primer elemento
       operadores = elementos[1:] #El resto de elementos son operadores
       operadores[-1] = operadores[-1][:-1]
       print(operacion)
       print(operadores)
       #Hacemos que resultado sea el primer elemento y "operando" el resto
       resultado = int(operadores[0]) 
       j = 1
       if operacion == "suma":
           while j < len(operadores):
               operando = int(operadores[j]) 
               resultado = calculadora.suma(resultado, operando)
               j = j +1


       i = i + 1
        
        

    



