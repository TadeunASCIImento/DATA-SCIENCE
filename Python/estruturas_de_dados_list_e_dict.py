# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:35:31 2020

@author: TadeunASCIImento
"""

# LIST

# Exemplo de declaração de listas
clientes = ["Leonardo", "Ricardo", "Monica", "Fernanda", "Luiza"]
times = ["Sao Paulo","Palmeiras", "Santos", "Corinthians"]
produtos = []
codigos = [0,1,1,2,3,4,5,6,7,8,9,10]


# Acessando dados de uma lista pelo indíce
print('-------------------------------')
print(clientes[2])
print(times[0])
print(codigos[7])



# Visualizando elementos de uma lista com
# o comando For
print('-------------------------------')
for cliente in clientes:
    print(cliente)



# Visualizando a lista com o comando print
print('-------------------------------')
print(clientes)
print(times)
print(codigos)


# Manipulando dados de uma lista

# Adicionando um novo elemento a lista com
# o comando append
print('-------------------------------')
clientes.append('Tadeu')
print(clientes)


# Adicionando novo elemento em uma posição
# específica com o comando insert
print('-------------------------------')
clientes.insert(2,'Angela')
print(clientes)


# Removendo dados de uma lista.
print('-------------------------------')
clientes.remove('Ricardo')
print(clientes)


# Alterando valor de um determinada posição
# da lista
print('-------------------------------')
clientes[0] = 'Marcela'
print(clientes)


# Contando elementos com o mesmo valor de uma lista
print('-------------------------------')
contador = codigos.count(1)
print('Número de elementos com valor 1:',contador)


# Visualizando a quantidade de elementos em uma lista
print('-------------------------------')
print('Número de elementos na lista clientes:',len(clientes))

# Ordenando dados de uma lista com o com comando
# sort
print('-------------------------------')
clientes.sort()
print(clientes)

# Verificando a existência de um dado específico na lista
print('-------------------------------')
if'Fernanda' in clientes:
    print('Cliente encontrado')

if'Matheus' not in clientes:
    print('Ciente não localizado')


# DICT

# Exemplo_1
print('-------------------------------')
dic_alunos = {"matricula":22172020,"nome":"João","idade":20,"nota1":8,"nota2":7.5};
print("Matricula:",dic_alunos["matricula"])

print('-------------------------------')
dic_alunos["matricula"] = 22172021
print("dic_alunos[matricula] - após dic_alunos[ matricula] = 22172021 ",dic_alunos["matricula"])

print('-------------------------------')
# Visualizando dados em dict_alunos
for x,y in dic_alunos.items():
    print(x,y)

# Verificando se uma determinada chave exixte no dict
print('-------------------------------')
if("matricula" in dic_alunos):
    print("matricula",dic_alunos["matricula"])

# Verificando se determinado valor existe no dict
print('-------------------------------')
if("João" in dic_alunos.values()):
    print("João pertence ao dic_alunos")

# Removendo elementos do dict
print('-------------------------------')
del dic_alunos["nome"]
print(dic_alunos)

# Incluindo novo elemento ao dict
print('-------------------------------')
media = (dic_alunos["nota1"]+dic_alunos["nota2"])/2
dic_alunos["media final"] = media
print("Após inclusão de media final",dic_alunos)
