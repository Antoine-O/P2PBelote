import random

def estegal(nombre1,nombre2):
    egal = nombre2 == nombre1
    return egal

def nombre_egal_app():
    nombreInput1 = input("Nombre 1?")
    nombreInput2 = input("Nombre 2?")
    if estegal(nombreInput1,nombreInput2):
        print("Egal")
    else :
        print("Différent")

