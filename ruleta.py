#Crear una ruleta
import os
import random
import funciones
saldo=10000
mje=""
jugar= True
opcion=0
apuesta=0
bolilla=0
color=""
colorBolilla=""

while (jugar == True):
    os.system("cls")
    msj= "Su saldo es "+str(saldo)
    print(msj)
    msj= "1. Jugar 2. Salir"
    print(msj)
    opcion= int(input(""))
    if opcion== 2:
        jugar= False
    if opcion== 1:
        msj= "Ingresar valor a apostar: "
        print (msj)
        apuesta= int(input(""))
        if apuesta <= saldo:
            msj="Elegir color. 1) Verde. 2)Rojo. 3)Negro"
            print(msj)
            opcion= int(input(""))
            bolilla=random.randint(0,6)
            if (opcion==1):
                color="VERDE"
            if (opcion==2):
                color= "ROJO"
            if (opcion==3):
                color= "NEGRO"
            colorBolilla= funciones.obtenerColor(bolilla)
            if (color == colorBolilla):
                print("Ganaste!")
                saldo= saldo+ apuesta
            else:
                saldo= saldo-apuesta
                print("Ups, lo siento")
            msj= "Número: "+str(bolilla)+" "+ colorBolilla
            print(msj)
            car= input("Presione una teclar para continuar")
            