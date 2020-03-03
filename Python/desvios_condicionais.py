# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 23:40:26 2020

@author: TadeunASCIImento
"""



# Desvio condicional simples

var_1 = 10
var_2 = int(input("informe o valor de var_2: "))
var_3 = 40
var_4 = 0
if(var_1==var_2):
    var_3 = var_1+var_2
    var_3 = var_3 + 5
var_4 = var_3 + 20
print(var_4)


# Desvio condicional composto

var_5 = 45
var_6 = int(input("informe o valor de var_6: "))
var_7 = 49
var_8 = 0
if(var_5==var_6):
    var_7 = var_5+var_6
    var_7 = var_7+4
else:
    var_7 = var_5-var_6
    var_7 = var_7 + 4
var_8 = var_7 + 10
print(var_8)


# Desvio condicional encadeado

var_9 = 0
var_10 = int(input("informe o valor de var_10:"))
if(var_10 == 1):
    var_9 = 10
elif(var_10 == 2):
    var_9 = 20
elif(var_10 == 3):
    var_9 = 30
elif(var_10 == 4):
    var_9 = 40
elif(var_10 == 5):
    var_9 = 50
else:
    var_9 = 100
print(var_9)
