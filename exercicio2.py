# -*- coding: utf-8 -*-

# Programa que recebe duas notas e calcula a media delas.
# Se for maior que 6 diz que é aprovado se for menor diz que é reprovado 
 
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