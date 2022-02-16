#Consola_%Grasa

import calculadora_indices as calc

def ejec_calcular_porgras()->None:
    weight = float(input("Ingrese su peso en kg: "))
    height = float(input("Ingrese su altura en mts: "))
    age = int(input("Ingrese su edad en años: "))
    valor_genero = float(input("Ingrese el valor 10.8 en caso de ser hombre o 0 en caso de ser mujer: "))
    answer = calc.calcular_porcentaje_grasa(weight,height,age,valor_genero)
    print()
    print (answer,"%")

def iniciar_calculadora_porcentaje_grasa()->None:
    print("Bienvenido a la calculadora del porcentaje de grasa")
    ejec_calcular_porgras()

#Bloque_Principal
iniciar_calculadora_porcentaje_grasa()