# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 23:21:33 2020

@author: TadeunASCIImento
"""

#Importa a classe AlunoEscL de aluno.py
from aluno import AlunoEscL

#Cria um objeto aluno1 do tipo AlunoEscL
aluno1 = AlunoEscL(1,"João","CC",9.5,5.8,8.7)

#Altera o nome de Joao para John
aluno1.setNome("John")

#Cria um objeto aluno1 do tipo AlunoEscL
aluno2 = AlunoEscL(2,"Mary","SI",9.8,4.5,8.1)

# Calcula a media de cada aluno
aluno1.calcularMedia()
aluno2.calcularMedia()

# Recupera o nome de cada aluno
nome1 = aluno1.getNome()
nome2 = aluno2.getNome()

# Recupera o valor da media de cada aluno
media1 = aluno1.getMedia()
media2 = aluno2.getMedia()

#Exibe o nome e media dos alunos
print("Média do aluno(a)",nome1," : ",media1)
print("Média do aluno(a)",nome2," : ",media2)
