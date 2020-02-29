# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 23:21:39 2020

@author: TadeunASCIImento
"""

# Declarando as variáveis
var_str = "Hello World"
var_int = 37
var_flt = 1.76
var_bol = True

# Vizualizando tipo de dado em cada variável
print(type(var_str))
print(type(var_int))
print(type(var_flt))
print(type(var_bol))

# Visualizando conteúdo das variáveis
print(var_str)
print(var_int)
print(var_flt)
print(var_bol)

# Concatenando informações
nome = 'Tadeu'
curso = 'Ciência da Computação'
ano = 2017
print('O aluno ',nome,'iniciou a faculdade de ',curso,'no ano de ',ano,'.')

# Lendo dados do teclado
print('Calculo da idade')
ano_atual = int(input('informe o ano atual ? '))
ano_nasc = int(input('informe o ano de nascimento ? '))
print('A idade é ',(ano_atual-ano_nasc),'anos.')

var_1 = 200
var_2 = 145
var_3 = 298
var_4 = 123

#Operadores aritméticos,relacionais e lógicos
var_soma = var_1+var_2+var_3
print('valor da soma é:',var_soma)
print(type(var_soma))

var_res = var_soma/2
print('valor da soma dividido po 2:',var_res)

print(type(var_res))

print(var_soma>var_res)
print(var_res>var_soma)
print(var_res+var_soma>1000)
print(var_soma>100 and var_res>50)
print(var_res<400 or var_soma>200)
print(not var_res+200==var_soma)
print(var_res<=400)
print(var_soma>=1000)
print(var_soma != var_res)
print(var_soma%2)
