#Consola_IMC

import calculadora_indices as calc

def ejec_calcular_imc()->None:
    weight = float(input("Ingrese su peso en kg: "))
    height = float(input("Ingrese su altura en mts: "))
    answer = calc.calcular_IMC(weight,height)
    print()
    print (answer)

def iniciar_calculadoraIMC()->None:
    print("Bienvenido a la calculadora del IMC")
    ejec_calcular_imc()

#Bloque_Principal
iniciar_calculadoraIMC() 