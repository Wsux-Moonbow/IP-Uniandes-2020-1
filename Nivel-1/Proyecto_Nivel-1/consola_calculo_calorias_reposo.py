#Consola_CaloriasReposo

import calculadora_indices as calc

def ejec_calcular_calrep()->None:
    weight = float(input("Ingrese su peso en kg: "))
    height = float(input("Ingrese su altura en cm: "))
    age = int(input("Ingrese su edad en años: "))
    genre = float(input("Ingrese el valor 5 en caso de ser hombre o -161 en caso de ser mujer: "))
    answer = calc.calcular_calorias_en_reposo(weight,height,age,genre)
    print()
    print(answer,"cal")

def iniciar_calculadora_CaloRep()->None:
    print("Bienvenido a la calculadora de calorias en reposo")
    ejec_calcular_calrep()

#Bloque_Principal
iniciar_calculadora_CaloRep() 