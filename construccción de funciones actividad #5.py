#!/bin/python3

# definir función


def completeDivision(numerator, denominator):
    if (denominator ==0):
        print("error")
    else:
        print("cociente", numerator // denominator)
        print("residuo", numerator % denominator)

completeDivision(50,8)
print("--------------")
completeDivision(2,0)
print("---------------")
completeDivision(2500,4)
print("---------------")


def sumar(sumando1, sumando2):
    print("resultado de la suma", sumando1+sumando2)
def resta(minuendo, sustraendo):
    print("resultado de la resta", minuendo-sustraendo)
def multiplicar(multiplicando,multiplicador):
    print("resultado de la multiplicacion", multiplicando*multiplicador)
def potenciar(base, exponente):
    print("resultado de la potencia", base**exponente)

sumar(20,45)
print("----------")
resta(50,30)
print("----------")
multiplicar(70,50)
print("----------")
potenciar(20,9)
print("----------")

