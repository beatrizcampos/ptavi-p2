#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calculadora = Calculadora()

    if sys.argv[2] == "suma":
        result = calculadora.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadora.resta(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
