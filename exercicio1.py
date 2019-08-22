# -*- coding: utf-8 -*-
idade = int(input("Digite sua idade: "))

def olhaIdade(idade):
    if idade >= 18:
        print("Você é maior de idade.")
    elif idade >= 0 and idade < 18:
        print("Você é menor de idade.")
    else:
        print("Você não digitou sua idade.")

olhaIdade(idade)
