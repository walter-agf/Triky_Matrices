#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:59:14 2020
@author: Gualteros
"""
from FuncionesO import continuar,dice,impre,resul,inicio,terminar
from Funciones import imprimir,play,eliminar,empate
import random
conti = True
jug1,jug2,ficha1,ficha2,conti = inicio (conti)
conti = True
while conti == True :
    print ("\nIngrese el tamaño de la cuadricula (#NOTA)(Debe ingresar valores enteros)")
    m = int(input("\nFilas = "))
    n = int(input("Columnas = "))
    aonti = True
    while aonti == True:
        turn = random.randint(0,1)
        ma,sec,verti = dice(m,n)# ma = Matriz de dibujo # sec = segmento de dibijo # verticales de dibujo
        horiz,val= impre(ma,sec)# horiz = Horizontaoles de posciciones # Matriz de posiciones
        filas,columnas,diagonales = resul(val,m,n) #filas = resultados en filas; columnas = resultados en columnas; diagonales = resultados en diagonales
        filas1,columnas1,diagonales1 = resul(val,m,n)
        filas2,columnas2,diagonales2 = resul(val,m,n)
        pos = []
        while aonti == True:
            print ("\n"*12)
            if turn == 0:
                imprimir(ma,sec)
                dedal,posf,posc,pos = play (jug1,verti,horiz,pos)
                ma [posf][posc] = ficha1
                filas1,columnas1,diagonales1 = eliminar(dedal,filas1,columnas1,diagonales1)
                filas,columnas,diagonales = eliminar(dedal,filas,columnas,diagonales)
                b = empate(filas,columnas,diagonales)
                if b == True:
                    imprimir(ma,sec)
                    print ("\n\n Se declara EMPATE")
                    break
                if [] in filas1 or [] in columnas1 or [] in diagonales1:
                    imprimir(ma,sec)
                    print ("\n\nFelicidades el Jugador ",jug1," Ha GANADO")
                    break
                turn = 1
            elif turn == 1:
                imprimir(ma,sec)
                dedal,posf,posc,pos = play (jug2,verti,horiz,pos)
                ma [posf][posc] = ficha2
                filas2,columnas2,diagonales2 = eliminar(dedal,filas2,columnas2,diagonales2)
                filas,columnas,diagonales = eliminar(dedal,filas,columnas,diagonales)
                b = empate(filas,columnas,diagonales)
                if b == True:
                    imprimir(ma,sec)
                    print ("\n\n Se declara EMPATE")
                    break
                if [] in filas2 or [] in columnas2 or [] in diagonales2:
                    imprimir(ma,sec)
                    print ("\n\nFelicidades el Jugador [ ",jug2," ] Ha GANADO")
                    break
                turn = 0
        print ("\nDesea continuar : ")
        conti = continuar(conti)
        aonti,jug1,jug2,ficha1,ficha2,conti = terminar (jug1,jug2,ficha1,ficha2,conti,inicio,aonti)
print ("\nGracias por Jugar :D")
