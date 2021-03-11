#Consola_CaloriasActividad

import calculadora_indices as calc

def ejec_calcular_calact()->None:
    weight = float(input("Ingrese su peso en kg: "))
    height = float(input("Ingrese su altura en cm: "))
    age = int(input("Ingrese su edad en años: "))
    genre = float(input("Ingrese el valor 5 en caso de ser hombre o -161 en caso de ser mujer: "))
    print()
    print("Ahora va a ingresar el valor que corresponda a la actividad fisica que realice semanalmente: ")
    print()
    print(" -Si hace poco o ningun ejercicio en la semana, ingrese el valor 1.2")
    print()
    print(" -Si hace ejercicio ligero (1 a 3 dias en la semana), ingrese el valor 1.375")
    print()
    print(" -Si hace ejercicio moderado (3 a 5 dias a la semana), ingrese el valor 1.55")
    print()
    print(" -Si hace ejercicio de nivel deportista (6 a 7 dias en la semana), ingrese el valor 1.725")
    print()
    print(" -Si hace ejercicio de nivel atleta (Entrenamientos por la mañana y la tarde), ingrese el valor 1.9")
    activity = float(input("Ingrese el valor: "))   
    answer = calc.calcular_calorias_en_actividad(weight,height,age,genre,activity)
    print()
    print (answer,"cal")

def iniciar_calculadora_CaloAct()->None:
    print("Bienvenido a la calculadora de calorias en actividad")
    ejec_calcular_calact()

#Bloque_Principal
iniciar_calculadora_CaloAct() 