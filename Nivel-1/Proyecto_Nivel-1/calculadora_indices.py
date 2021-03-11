#Modulo

def calcular_IMC (peso:float, altura:float)->float:
    IMC = (peso/((altura)**2))
    return round(IMC,2)

def calcular_porcentaje_grasa (peso:float, altura:float, edad:int, valor_genero:float)->float:
    PorcentajeGrasa = 1.2*calcular_IMC(peso, altura)+0.23*edad-5.4-valor_genero
    return round(PorcentajeGrasa,2)

def calcular_calorias_en_reposo (peso:float, altura:float, edad:int, valor_genero:float)->float:
    tmb = (10*peso)+(6.25*altura)-(5*edad)+valor_genero
    return round(tmb,2)

def calcular_calorias_en_actividad (peso:float, altura:float, edad:int, valor_genero:float, valor_actividad:float)->float:
    tmbA = (calcular_calorias_en_reposo(peso,altura,edad,valor_genero))*valor_actividad
    return round(tmbA,2)

def consumo_calorias_recomendado_para_adelgazar (peso:float, altura:float, edad:int, valor_genero:float)->str:
    tmb = calcular_calorias_en_reposo(peso,altura,edad,valor_genero)
    ValorVein = round(((tmb*80)/100),2)
    ValorQuin = round(((tmb*85)/100),2)
    return ("Para adelgazar es recomendado que consumas entre "+str(ValorVein)+" y "+str(ValorQuin)+" calorias al dia.") 