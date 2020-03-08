# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 23:03:37 2020

@author: TadeunASCIImento
"""

class AlunoEscL:

    # __init__ metodo Contrutor da classe AlunoEscL

    def __init__(self,matricula,nome,curso,nota1,nota2,nota3):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = 0

    # Metodos getters

    def getMatricula(self):
        return self.matricula

    def getNome(self):
        return self.nome

    def getCurso(self):
        return self.curso

    def getNota1(self):
        return self.getNota1

    def getNota2(self):
        return self.getNota2

    def getNota3(self):
        return self.nota3

    def getMedia(self):
        return self.media


    # Metodos setters

    def setMatricula (self, matricula):
        self.matricula = matricula

    def setNome(self, nome):
        self.nome = nome

    def setCurso(self, curso):
        self.curso = curso

    def setNota1(self, nota1):
        self.nota1 = nota1

    def setNota2(self, nota2):
        self.nota2 = nota2

    def setNota3(self, nota3):
        self.nota3 = nota3

    # Declarando metodo para calculo da media do aluno
    def calcularMedia(self):
        if(self.curso == "CC"):
            self.media = (self.nota1+self.nota2+self.nota3)/3
        else:
            self.media = (self.nota1+self.nota2+(2*self.nota3))/4
