#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:26:27 2020

@author: Gualteros
"""
def imprimir(ma,sec):
    num = 1
    for i in range(0,len(ma)):
        lis = ma[i]
        cont = 0
        while cont < len(lis):
            print (lis[cont],end="")
            cont += 1
        if str(i) in sec :
            cont = 0
            print ("              ",end="")
            if num <= 9 :
                while cont < (len(lis)/3):
                    print ("▌ ",end="")
                    print ("",num,"",end="")
                    print ("▐",end="")
                    num += 1
                    cont += 1
            else:
                while cont < (len(lis)/3):
                    print ("▌",end="")
                    print ("",num,"",end="")
                    print ("▐",end="")
                    num += 1
                    cont += 1
        print ("")
def play (jug,verti,horiz,pos):
    print ("\n",jug,"Ingrese su proxima jugada")
    dedal = (int(input("----> ")))
    while dedal > horiz[-2][-1] or dedal in pos:
        print ("Valor fuera del rango ó valor ya ingresado --- reingrese")
        dedal = (int(input("-----> ")))
    pos.append(dedal)
    posf = 0
    sig = 0
    while posf == 0:
        if dedal in horiz[sig]:
            posf = sig
        else:
            sig += 1
    posc = horiz[posf]
    posc = posc.index(dedal)
    posc = verti[posf][posc]
    return dedal,posf,posc,pos
def eliminar(dedal,filas,columnas,diagonales):
    d = 0
    while d != len(filas):
        if dedal in filas[d]:
            filas[d].remove(dedal)
            d += 1
        else:
            d += 1
    d = 0
    while d != len(columnas):
        if dedal in columnas[d]:
            columnas[d].remove(dedal)
            d += 1
        else:
            d += 1
    d = 0
    while d != len(diagonales):
        if dedal in diagonales[d]:
            diagonales[d].remove(dedal)
            d += 1
        else:
            d += 1
    return filas,columnas,diagonales
def empate(filas,columnas,diagonales):
    datos = []
    datos.append(filas)
    datos.append(columnas)
    datos.append(diagonales)
    emp = 0
    for i in range (0,len(datos)):
        dat = datos[i]
        b = 0
        fi = 0
        while b != len(dat):
            if 0 == len(dat[b]):
                fi += 1
            b += 1
        if fi == len(filas):
            emp += 1
    if emp == len(datos)-1:
        b = True
    else:
        b = False
    return b
