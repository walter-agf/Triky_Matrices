#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:14:25 2020
@author: gualteros
"""
def continuar (conti):
    s = False
    while s == False:
        cos = (input("[ 0 = SI] [ 1 = NO ]---> "))
        if cos == "1" :
            conti = False
            s = True
        elif cos == "0" :
            conti = True
            s = True
        else:
            print ("Valor indeterminado, reingrese")
    return conti
"""
g = True
g = continuar (g)
print (g)
"""
def dice(m,n):
    m = m * 3
    filas = []
    pri = []
    sec = []
    sed = []
    ter = []
    vertical = []
    ini = 0
    while ini < m:
        pri.append(str(ini))
        ini += 3
    ini = 1
    while ini < m:
        sed.append(ini)
        sec.append(str(ini))
        ini += 3
    ini = 2
    while ini < m:
        ter.append(str(ini))
        ini += 3
    for san in range (0,m):
        colum = []
        ver = []
        if str(san) in pri:
            d = 0
            while d < (n):
                colum.append("▬▬")
                colum.append("▬▬▬")
                colum.append("▬▬▬")
                d += 1
            vertical.append(ver)
        if str(san) in sec:
            d = 0
            while d < (n):
                colum.append("▌")
                colum.append("      ")
                colum.append("▐")
                d += 1
            vertical.append(sed)
        if str(san) in ter:
            d = 0
            while d < (n):
                colum.append("▬▬")
                colum.append("▬▬▬")
                colum.append("▬▬▬")
                d += 1
            vertical.append([])
        filas.append(colum)
    return filas,sec,vertical
"""
m = 3
n = 3
h,sec,verti = dice(m,n)
print (h)
print (sec)
print (verti)
"""
def impre (ma,sec):
    num = 1
    pos = []
    valores = []
    for i in range(0,len(ma)):
        lis = ma[i]
        cont = 0
        while cont < len(lis):
            print (lis[cont],end="")
            cont += 1
        if str(i) in sec :
            cont = 0
            print ("              ",end="")
            fil = []
            if num <= 9 :
                while cont < (len(lis)/3):
                    print ("▌ ",end="")
                    print ("",num,"",end="")
                    print ("▐",end="")
                    fil.append(num)
                    num += 1
                    cont += 1
                valores.append(fil)
                pos.append(fil)
            else:
                while cont < (len(lis)/3):
                    print ("▌",end="")
                    print ("",num,"",end="")
                    print ("▐",end="")
                    fil.append(num)
                    num += 1
                    cont += 1
                valores.append(fil)
                pos.append(fil)
        else :
            pos.append([])
        print ("")
    return pos,valores
"""
d,valores = impre (h,sec)
print (d)
print (valores)
"""
def resul(val,m,n):
    if m > 4 or n > 4:
        ga = 4
    else:
        ga = 3
    diagonales = []
    filas = []
    columnas = []
    num = len(val)
    nu = num
    for i in range (0,(m+n)-1):
        di = []
        if nu != 0 :
            nu -= 1
            no = 0
        elif no == num:
            z = 1
            no = z
        else:
            z += 1
            no = z
        larg = nu
        while larg != num:
            c = val[larg]
            if no < len(c):
                di.append(c[no])
                larg += 1
                no += 1
            else:
                larg += 1
                no += 1
            if len(di) > ga and larg == num:
                    for i in range (0,len(di)-2):
                        df = di[i:i+ga]
                        if len(df) == ga:
                            diagonales.append(df)
            if len(di) == ga and larg == num:
                diagonales.append(di)
    nu = num
    for i in range (0,(m+n)-1):
        di = []
        if nu != 0:
            nu -= 1
            no = num - 1
        else:
            z -= 1
            no = z
        larg = nu
        while larg != num:
            c = val[larg]
            if no >= 0:
                di.append(c[no])
                larg += 1
                no -= 1
            else:
                larg += 1
                no -= 1
            if len(di) > ga and larg == num:
                    for i in range (0,len(di)-2):
                        df = di[i:i+ga]
                        if len(df) == ga:
                            diagonales.append(df)
            if len(di) == ga and larg == num:
                    diagonales.append(di)
    nu = num
    for i in range (0,m):
        c = val[i]
        for x in range (0,len(c)):
            df = c[x:x+ga]
            if len(df) == ga:
                filas.append(df)
    for i in range (0,n):
        df = []
        for fi in range (0,m):
            c = val[fi]
            df.append(c[i])
        columnas.append(df)
    return filas,columnas,diagonales
"""
filas,columnas,diagonales = resul(valores,m,n)
print (filas,"\n")
print (columnas,"\n")
print (diagonales,"\n")
"""
def inicio (conti):
    x = open("intro.txt","r")
    g = x.read()
    print(g)
    x.close()
    print ("Ingrese el nombre de los dos jugadores")
    print ("(#NOTA) EL jugador uno escoge la ficha")
    jug1 = (input("Jugador 1 ---> "))
    jug2 = (input("Jugador 2 ---> "))
    while conti == True :
        print ("\n\n",jug1,"¿Con que ficha deseas Jugar? [ X ] [ O ]")
        ficha = (input("-----> "))
        if ficha in "Xx":
            ficha1 = "  X   "
            ficha2 = "  O   "
            conti = False
        elif ficha in "O0oóÓ":
            ficha1 = "  O   "
            ficha2 = "  X   "
            conti = False
        else:
            print ("Valor Incorrecto, reingrese valor")
    return jug1,jug2,ficha1,ficha2,conti
"""
conti = True
jug1,jug2,ficha,conti = inicio (conti)
"""
def terminar(jug1,jug2,ficha1,ficha2,conti,inicio,aonti):
    if conti == True:
        print ("\n¿Desea rehacer la Cuadricula ó cambiar los nombres? ")
        print ("\nRehacer cuadricula                                      --- [ 1 ]")
        print ("Cambiar nombres                                         --- [ 2 ]")
        print ("Cambiar nombres y rehacer cuadricula (ó cambair ficha)  --- [ 3 ]\n")
        print ("No quiero hacer ningun cabio                            --- [ 0 ]")
        obciones = (input("---------> "))
        if obciones == "1":
            aonti = False
        elif obciones == "2":
            jug1,jug2,ficha1,ficha2,conti = inicio (conti)
            conti = True
        elif obciones == "3":
            aonti = False
            jug1,jug2,ficha1,ficha2,conti = inicio (conti)
            conti = True
    else:
        aonti = False
    return aonti,jug1,jug2,ficha1,ficha2,conti
