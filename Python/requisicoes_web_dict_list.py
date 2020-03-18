# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:07:03 2020

@author: TadeunASCIImento
"""

# Utilizando dicts e lists em requisições web

# Link do site utilizado nos testes http://omdbapi.com

import json
import requests
# url do site com os dados para tratamento
url_site = "http://www.omdbapi.com/?apikey=f8fe7487&t=";

# transformnado a resposta em um objeto Python(dict)
def transforma(titulo_filme):
    requisicao = requests.post(url_site+titulo_filme)
    return json.loads(requisicao.text)

filme = input('Informe o filme em inglês?')
if filme == '':
    filme = 'Blade Runner'
dicionario_filme = transforma(filme)

# Exibindo apenas algumas informações do filme
print('\n\n\tDADOS DO FILME\n')
if(dicionario_filme['Response']=='False'):
    print('Filme não localizado')
else:
    print('Título: '+dicionario_filme['Title'])
    print('Ano de produção: '+dicionario_filme['Year'])
    print('Genero: ' +dicionario_filme['Genre'])
    print('Direção: '+dicionario_filme['Director'])
    print('Duração: '+dicionario_filme['Runtime'])
    print('Produtora: '+dicionario_filme['Production'])

atores = dicionario_filme['Actors'].split(', ')
exibe_ator = False
for ator in atores:
    if not exibe_ator:
        print('\nAtores:'+ator)
        exibe_ator = True
    else:
        print('      :'+ator)

avaliacoes = dicionario_filme['Ratings']
for avaliacao in avaliacoes:
    fonte = avaliacao['Source']
    valor = avaliacao['Value']
print('\nAvaliações\nFonte: '+fonte+' valor: '+valor)
