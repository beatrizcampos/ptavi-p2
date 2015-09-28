#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):
    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            sys.exit("Error: Division by zero is not allowed")


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calculadora = CalculadoraHija()

    if sys.argv[2] == "suma":
        result = calculadora.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadora.resta(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = calculadora.multiplicar(operando1, operando2)
    elif sys.argv[2] == "divide":
        result = calculadora.dividir(operando1, operando2)
    else:
        sys.exit('Sólo puede ser sumar,restar, multiplicar o dividir.')

    print(result)
