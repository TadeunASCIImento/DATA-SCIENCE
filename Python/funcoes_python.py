# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:26:26 2020

@author: TadeunASCIImento
"""

# Métodos e funções em Python

# Exemplo de utilização de funções

# Declarando as funções

def finalizar():
    msg = 'Programa finalizado com sucesso!'
    return msg

def exibirMensagem(nome,media):
    print("O aluno",nome,"obteve a média:",media)

def resultadoFinal(media):
    if(media>=6):
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")

def calcularMedia(nota1,nota2):
    calculo = (nota1+nota2)/2
    return calculo

def verificaMaiorValor(lista):
    maiorValor = 0
    for num in lista:
        if(num>maiorValor):
            maiorValor = num
    return maiorValor

listaNumeros = [13,5,78,1,59,78,35,654,532]
maior = verificaMaiorValor(listaNumeros)
print("Maior valor encontrado na lista de numeros foi:",maior)


nomeAluno = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
media = calcularMedia(nota1,nota2)
exibirMensagem(nomeAluno,media)
resultadoFinal(media)
msgFim = finalizar()
print(msgFim)
