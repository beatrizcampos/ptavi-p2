#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija


if __name__ == "__main__":
    fich = open(sys.argv[1],'r')
    linea = fich.readlines() 
    lineas = len(linea) ##numero de lineas que hay
    print(lineas)
    elementos = linea[0].split(',')##elementos que hay en linea
    print(elementos) 
    print(len(elementos)) ##numero elementos en linea

    calculadora = calcoohija.CalculadoraHija()
    i = 0
    while i < lineas:
        operar(
        
        

    



