#Consola_CaloriasAdelgazar

import calculadora_indices as calc

def ejec_calcular_calAde()->None:
    weight = float(input("Ingrese su peso en kg: "))
    height = float(input("Ingrese su altura en cm: "))
    age = int(input("Ingrese su edad en años: "))
    genre = float(input("Ingrese el valor 5 en caso de ser hombre o -161 en caso de ser mujer: "))
    answer = calc.consumo_calorias_recomendado_para_adelgazar(weight,height,age,genre)
    print()
    print(answer)

def iniciar_calculadora_CaloAdel()->None:
    print("Bienvenido a la calculadora de calorias para adelgazar")
    ejec_calcular_calAde()

#Bloque_Principal
iniciar_calculadora_CaloAdel() 