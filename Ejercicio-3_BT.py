# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 20:08:54 2021

@author: Braulio
"""
#Programa que permita encontrar valores máximos y mínimos dentro de los valores de un diccionario
dic1={'Raul':34,'Paula':19,'Jorge':43,'Richard':10,'Diana':3,'Isabel':76,'Gustavo':12,'Diego':37}
dic2={'tplA':(4,-12,56,-34,98,102),'tplB':(9,0,1,10,-3,14),'tlpC':(87,12,56,987,-61)}
dic3={'val1':-12.5,'val2':12.5,'val3':83,'val4':2.1,'val5':23,'val6':100,'val7':13.4,'val8':92}
dic4={'lst1':[4,6,-12,56,-9,5.7,33,100],'lst2':[9,0,81,-2,-56,],'lst3':[12,31,87,1,0,4,-11]}

def maxmin(dicc):
    if dicc==1:
        valores=list(dic1.values())
    if dicc==2:
        valoresd2=list(dic2.values())
        valores=list(valoresd2[0])+list(valoresd2[1])+list(valoresd2[2])
    if dicc==3:
        valores=list(dic3.values())
    if dicc==4:
        valoresd2=list(dic4.values())
        valores=list(valoresd2[0])+list(valoresd2[1])+list(valoresd2[2])
    flag3=1
    while flag3==1:
        nmin=int(input('Digite el número de máximos que desea mostrar:'))
        nmax=int(input('Digite el número de mínimos que desea mostrar:'))
        if (nmax+nmin)>len(valores):
            print(f'\nValores de max y min exceden el tamaño del arreglo:{len(valores)}.\
 Por favor ingrese nuevamente los números.')
        else:
            flag3=2
            valores.sort()
            lst_min=[]
            lst_min=valores[0:nmin]
            valores.sort(reverse=True)
            lst_max=[]
            lst_max=valores[0:nmax]
            lst_max.sort()
            salida=lst_min+lst_max
            print('\nValores calculados en formato LISTA:',salida)
            print('Valores calculados en formato TUPLA:',tuple(salida))
            
        
    return valores


flag1=1
while flag1==1:
    print('\nElija una opción:\n1) Demostración del cálculo de máximos y mínimos en diccionarios.\n2) Salir.')
    opc1=int(input('Opción:'))
    flag2=1
    if opc1==1:
        while flag2==1:
            print('\nElija un diccionario para la demostración:\n\n\
1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}\n\
2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}\n\
3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}\n\
4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}')
            opc2=int(input('Opción:'))
            if opc2==1:
                maxmin(1)
                flag2=2
            elif opc2==2:
                maxmin(2)
                flag2=2
            elif opc2==3:
                maxmin(3)
                flag2=2
            elif opc2==4:
                maxmin(4)
                flag2=2
            else: 
                print('\nERROR: POR FAVOR INGRESE UN VALOR DE LAS OPCIONES VALIDAS 1 al 4')
         
    elif opc1==2:
        flag1=2
        print('HASTA PRONTO!!')
    else:
        print('\nERROR: POR FAVOR INGRESE UN VALOR DE LAS OPCIONES VALIDAS 1 o 2')