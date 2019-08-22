# -*- coding: utf-8 -*-

# Programa que recebe dois valores e um operador matemático
# fazendo o calculo dos numeros de acordo com o operador digitado

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: ")) 
operadores = ["+", "-", "*", "/"]
print(operadores)
operador = input("Escolha um dos simbolos para realizar a operacao matemática: ")

def calculaNumeros(valor1, valor2, simbolo):
    if simbolo == "+":
        soma = valor1 + valor2
        return "A soma é " + str(soma)
    elif simbolo == "-":
        sub = valor1 - valor2
        return "A subtracao é " + str(sub)
    elif simbolo == "*":
        multi = valor1 * valor2 
        return "A multiplicacao é " + str(multi)
    elif simbolo == "/":
        divisao = valor1 / valor2 
        return "A divisao é " + str(divisao)
    else:
        print("Voce nao escolheu um dos operadores disponiveis")

print(calculaNumeros(num1, num2, operador))