# -*- coding: utf-8 -*-
av1 = float(input("Diga sua primeira nota: "))
av2 = float(input("Diga sua segunda nota: "))

def calculaMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6.0:
        print("Sua media foi: "+ str(media) +" Você está aprovado")
    elif media < 6.0:
        print("Sua media foi: "+ str(media) +" Você foi reprovado")
    else:
        print("Você não digitou sua nota")

calculaMedia(av1, av2)