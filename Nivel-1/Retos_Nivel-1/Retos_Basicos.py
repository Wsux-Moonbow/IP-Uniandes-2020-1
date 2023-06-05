'''
Aquí se encuentran la solucion de los retos de IP
SENECODE - AÑO 2020-1

--------------------------------------------------

NOTA IMPORTANTE: El formato de las funciones es distinto
al especificado en las clases de IP ejemplo:

Funcion que suma dos numeros enteros (Formato IP):

def suma(numero_1: int, numero_2: int)->int:
    resultado = numero_1 + numero_2                                            ¡ES LO MISMO!
    return resultado

Funcion que suma dos numeros enteros (Formato Simplificado):

def suma(numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado

--------------------------------------------------

El cambio no es significativo, el formato de IP está pensado
en la forma de programar de otros lenguajes donde tienes que
especificar el tipo de dato de los parametros y retorno de
la función. Ahora bien, en Python esto no hace falta, pero
si se puede controlar que tipo de datos salen y como interpretas
los datos. En el caso de la funcion anterior es exactamente la
misma en los dos formatos y no va a generar problemas en senecode.
'''
#Modulos utilizados en algunos retos

import math

'RETOS NIVEL 1'

'BASICOS:'

#Altura de una persona:

def altura_en_mts(pies, pulgadas):
    pulgas = pies * 12 + pulgadas
    metros = (pulgas * 2.54)/100
    return round(metros,2)

#Area de una habitación

def area_habitacion(largo, ancho):
    Area_Total = largo * ancho
    Area_Total_Redondeada = round(Area_Total, 2)
    return Area_Total_Redondeada

#IVA y propina

def calcular_iva_propina_total_factura(costo_factura):
    IVA = 19
    Propina = 10
    X = (IVA * costo_factura) / 100
    Y = (Propina * costo_factura) / 100
    Z = (X + Y + costo_factura)
    return(str(round(X)))+","+(str(round(Y)))+","+(str(round(Z)))

#Reciclaje de botellas plásticas

def calcular_pago_botellas(cant_pequenias, cant_grandes):
    ml500 = cant_pequenias * 0.10
    lmedio = cant_grandes * 0.25
    return round((ml500+lmedio),2)

#Saludo prolongado

def saludar_repetidas_veces(nombre, veces):
    saludo =  'H' + 'o' * veces + 'l' + 'a' * int(veces/2) + ' ' + nombre
    return saludo

#Suma de los primeros n enteros positivos

def suma_n_enteros_positivos(n):
    if n > 0:
        SumaEnteros = n * (n + 1) / 2
    return int(SumaEnteros)

#Tarifa de un taxi

def calcular_tarifa_taxi(kms_recorridos):
    tarifa = 4000
    metros = kms_recorridos * 1000
    recorrido = metros / 100
    aumento = recorrido * 82
    total = tarifa + aumento
    return round(total)

#Tiempo de descarga

def calcular_tiempo_descarga(velocidad, tamanio_archivo):
    Mbarch = (tamanio_archivo * 1000) * 8
    tots = Mbarch / velocidad
    tiempo = tots  / 60
    return round(tiempo)

#Unidades de tiempo a segundos

def tiempo_a_segundos(dias, horas, mins, seg):
    segd = dias * 86400
    segh = horas * 3600
    segm = mins * 60
    total = seg + segm + segh + segd
    return total

#Volumen de un cilindro

def volumen_cilindro(radio, altura):
    base  = 3.1416 * (radio**2)
    volumen = base *  altura
    return round(volumen,1)

'INTERMEDIOS:'

#Area de un poligono regular

def area_poligono_regular(num_lados, longitud):
    area = (num_lados * (longitud ** 2)) / (4 * math.tan(math.pi / num_lados))
    return round(area, 2)

#Area de un triangulo

def area_triangulo(s1, s2, s3):
    s = (s1+s2+s3)/2
    area = math.sqrt((s * (s-s1) * (s-s2) * (s-s3)))
    return round(area,1)

# Caida libre

def vel_en_caida_libre(altura):
    velocidad_final = math.sqrt(0**2 + (2* 9.8 * altura))
    return round(velocidad_final,2)

# Centrar texto en la terminal

def centrar_texto(cadena, ancho_terminal):
    calculus = (ancho_terminal - len(cadena))//2
    string = (' '*calculus+cadena)
    return string

# Costo de hervir agua

def costo_hervir_agua(masa_agua):
    deltaT = 100 - 20  # Diferencia de temperatura entre el agua hirviendo y la temperatura ambiente
    aguaC = 4.186  # Calor específico del agua en julios/gramo·°C
    energia = masa_agua * deltaT * aguaC  # Energía necesaria para calentar el agua
    valor = energia / (1000 * 3600)  # Conversión de julios a kilovatios-hora (kWh)
    valor *= 0.089  # Costo por kWh (valor aproximado)
    return round(valor, 4)  # Redondeo del costo a 4 decimales

# Distancia Manhattan

def calcular_distancia_manhattan(x1,y1,x2,y2):
    d = abs(x1-x2) + abs(y1-y2)
    return d

# Eficiencia combustible

def convertir_eficiencia_combustible(mpg):
    km = mpg * 1.6 # Convertir millas a kilómetros (1 milla = 1.6 kms)
    litros = 3.78 # Convertir galones a litros (1 galón = 3.78 litros)
    eficiencia = litros / km * 100 # Calcular eficiencia en litros por 100 kilómetros (L/100km)
    return round(eficiencia, 2)

# Indice de masa corporal

def calcular_BMI(peso_lb, altura_inch):
    BMI = (peso_lb*0.45)/((altura_inch*0.025)**2)
    return round(BMI,2)

# Ordenar 3 enteros

def ordenar_enteros(a, b, c):
    Grande = max(a,b,c)
    Pequeno = min(a,b,c)
    Medio = (a+b+c)-Pequeno-Grande
    return str(Grande)+","+str(Medio)+","+str(Pequeno)

# Pan del dia anterior

def calcular_total_pan_comprado(frescos, viejos):
    Vf = frescos * 450
    V_v = viejos * ((450 * 40) / 100)
    TpC = Vf + V_v
    return (TpC)