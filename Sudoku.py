# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 22:06:32 2021

@author: Danjour
"""

import numpy as np


print("----- Problema ----- ")

problema=[[0,4,3,0,0,0,0,0,9],
       [0,0,0,6,0,0,0,0,5],
       [0,0,0,0,0,4,1,0,0],
       [9,0,1,0,5,0,0,0,0],
       [0,0,0,7,2,6,0,0,0],
       [0,0,8,0,1,0,0,0,0],
       [0,1,0,0,0,0,7,2,0],
       [7,0,0,0,0,0,0,0,0],
       [2,0,0,0,0,5,0,6,0]]


print(np.matrix(problema))


def verificador(y,x,n):
    global problema
    for i in range(0,9): #Tamanho 
        if problema[y][i]==n:
            #Vai percorrer toda a linha da coluna para verificar se existe algum
            #número igual ao valor de entrada, se existir, ele retornará falso
            #e vai prosseguir para o próximo número.
            return False
    for i in range(0,9):
        if problema[i][x]==n:
            #Vai percorrer toda a coluna da coluna para verificar se existe algum
            #número igual ao valor de entrada, se existir, ele retornará falso
            #e vai prosseguir para o próximo número.
            return False
    x0=(x//3)*3
    #Agora vamos verificar somente o quadro do local desejado.
    y0=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            #Se dentro do quadrado tiver um número igual ao n, será retornado
            #false
            if problema[y0+i][x0+j]==n:
                return False
            #Caso nada disso seja falso, ele retornará verdadeiro.
    return True
                


def resolve():
    global problema
    for i in range(0,9):
        for j in range(0,9):
            if problema[i][j] == 0:
                for n in range(10):
                    if verificador(i,j,n):
                        problema[i][j]=n
                        resolve()
                        problema[i][j]=0
                return
    print(np.matrix(problema))
    
    
    
print("----- Solução -----")
resolve()