# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:48:57 2020

@author: TadeunASCIImento
"""

# Laço de repetição While.

continuar = 'c';

while(continuar=='c'):

    valor_a = float(input('Informe valor a: '))
    valor_b = float(input('Informe valor b: '))
    soma = valor_a+valor_b
    print('Soma de a e b é =',soma)
    continuar = input('Digite c para continuar, ou qualquer tecla para sair')
print('Programa finalizado')

# Laço For

# Exemplo_1

qtde = int(input('Quantidade de operações:'))

for(x) in range(0,qtde,1):
    valor_c = float(input('Informe valor c: '))
    valor_d = float(input('Informe valor d: '))
    multip = valor_c*valor_d
    print('Multiplicação de c e d = ',multip)
print('Programa finalizado!')

# Laço for exemplo_2

lista_cursos = ['Java','Python','PL/SQL','HTML5']
for curso in lista_cursos:
    print('Curso',curso)
