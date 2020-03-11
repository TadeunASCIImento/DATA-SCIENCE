# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 23:50:08 2020

@author: TadeunASCIImento
"""

# Requisições Web Python

import requests

# Link para o site: https://putsreq.com/
# utilizado nos testes de requisiçoes http.

requisicao = requests.post("https://putsreq.com/PHg8PVMBOOb0FVU8VYj3")
print(requisicao.text)

nome = input("Informe seu nome: ")
requisicao = requests.post("https://putsreq.com/PHg8PVMBOOb0FVU8VYj3?name="+nome)
print(requisicao.text)


# realizando uma requisição partir de uma url
url = input("informe a url do site")
requisicao = requests.post(url)
print(requisicao.text)
