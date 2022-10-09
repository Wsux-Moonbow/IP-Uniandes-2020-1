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