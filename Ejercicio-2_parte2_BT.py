# -*- coding: utf-8 -*-
"""
Programa que permite validar la contraseña introducida por un usuario
"""
print('\nPOR FAVOR INGRESE SU CONTRASEÑA CUMPLIENDO LAS SIGUIENTES CONDICIONES:\n')
print('Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.')
print('Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.')
print('Debe contener al menos un número entre 0 y 9.')
print('Debe contener un símbolo especial entre: $,%,*,@')
print('Tamaño mínimo de 5 caracteres y máximo de 15.')
cmin=('a','b','c','d','e','f','g','h','i','j')
cmay=('K','L','M','N','O','P','Q','R','S','T')
cnum=('0','1','2','3','4','5','6','7','8','9')
cesp=('$','%','*','@')
bucle=0
validacion=[0,0,0,0]
while bucle==0:
    password=input('Contraseña:')
    lst1=list(password)
    if len(lst1)>=5 and len(lst1)<=15:
        for i in lst1:
            if i in cmin:
                validacion[0]=1
            if i in cmay:
                validacion[1]=1
            if i in cnum:
                validacion[2]=1
            if i in cesp:
                validacion[3]=1
        if sum(validacion)==4:
            print('INGRESO EXITOSO DE CONTRASÑA')
            bucle=1
        else:
            print('La contrasena ingresada no cumple las condiciones solicitadas. Intente Nuevamente ')
    else:
        print('Tamaño incorrecto. Tamaño mínimo de 5 caracteres y máximo de 15.')
        