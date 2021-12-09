# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 18:47:45 2021

@author: Braulio
"""
#DECLARACION E INICIALIZACION DE VARIABLES
Datos_2021=[1,2,3,4,5,6,7,100,91,110,900,21,33,32,2,4,8,10,13,13,16,15,1302]
num_pares=[]
num_impares=[]
num_atip=[]
tupla=tuple(Datos_2021)
total_datos=len(tupla)
i=0
#BUCLE PARA LA SELECION DE NUMEROS PARES, IMPARES Y ATIPICOS
for x in Datos_2021:
    x%=2    #CALCULO DEL MODULO PARA DETERMINAR SI LA DIVISION ES ENTERA O NO
    if x==0:
        num_pares.append(tupla[i]) 
    else:
        num_impares.append(tupla[i]) 
    i+=1
    if i>=1 and i<total_datos-1:
        y=tupla[i+1]-tupla[i]
        if y>=100:  #ANALIZANDO LOS DATOS SE CONSIDERA VALORES ATIPICOS FUERA DE DEL RANGO DE DIFERENCIA DE 100 ENTRE UNOS DE OTROS
            num_atip.append(tupla[i+1])
print('Datos_2021=',tupla)
print('NÚMEROS PARES:',num_pares)
print('NÚMEROS IMPARES:',num_impares)
print('NÚMEROS ATÍPICOS:',num_atip)