#Juan Diego Quiros Gomez//Carnet:2024165546
#Reto 1
"""Entradas: 
capitalInicial (int)
tiempoEnAnnos (int)
tasaInteres (float)
Salidas:
interesSimple (float)
Restricciones:
1. El capital debe un valor
numérico mayor a 0.0
2. El tiempo debe estar
expresado en años > 0 y debe
ser entero
3. La tasa de interés es un
número decimal mayor a 0.0""" 
def calcularInteresSimple():

    capitalInicial = 0.0
    tiempoAnnos = 0
    tasaInteres = 0.0
    interesSimple = 0.0

    print("Indique el monto de Capital: ")
    capitalInicial = float(input())

    print("Indique el valor de tiempo en Annos: ")
    tiempoAnnos = int(input())

    print("Indique el valor de la tasa de interes: ")
    tasaInteres = float(input())

    interesSimple = capitalInicial * tiempoAnnos * tasaInteres

    print("El valor del interes simple es: ", interesSimple)

calcularInteresSimple()

#Reto 2
"""Entradas: 
litrosProducidos (int)
precioGalón (float)
Salidas:
montoProducciónLeche
(float)
Restricciones:
litrosProducidos es un valor
entero y > 0
precioGalón es un valor float y
> 0.0"""

def calcularMontoProduccionLeche ():
    litrosProducidos = 0.
    precioGalon = 0.0
    galonesProducidos = 0
    montoProduccionLeche = 0.0

    print("Indique la cantidad de leche producida en litros: ")
    litrosProducidos = int(input())

    print("Indique el valor del galon de leche ")
    precioGalon = float(input())

    galonesProducidos = litrosProducidos / 3.785
    montoProduccionLeche = galonesProducidos * precioGalon

    print("El monto total a pagar de leche es: ", montoProduccionLeche)

calcularMontoProduccionLeche()

#Reto3
"""Entradas: 
Largo (float)
Ancho (float)
Alto (float)
precioMetroCúbicoAgua
(float)
Salidas:
costoLlenarPiscina
(float)
Restricciones:
precioMetroCúbicoAgua, Largo, ancho
y alto son valores flotantes > 0.0"""
def calcularCostoLlenarPiscina ():
    largoPiscina = 0.0
    anchoPiscina = 0.0
    altoPiscina = 0.0
    volumenPiscina = 0.0
    precioMetroCubicoAgua = 0.0
    costoLlenarPiscina = 0.0

    print("Cuanto mide la piscina de largo?: ")
    largoPiscina = float(input())

    print("Cuanto mide la piscina de ancho?: ")
    anchoPiscina = float(input())

    print("Cuanto mide la piscina de alto?: ")
    altoPiscina = float(input())

    print("Precio metro cubico de agua: ")
    precioMetroCubicoAgua = float(input())

    volumenPiscina = largoPiscina * altoPiscina * anchoPiscina 

    costoLlenarPiscina = precioMetroCubicoAgua * volumenPiscina
    print("El costo de llenar la piscina es: ", costoLlenarPiscina)

calcularCostoLlenarPiscina()
  
#Reto 4
"""Entradas: 
horasLaboradas(int)
salarioPorHora (float)
horasExtra (int)
salarioPorHoraExtra
(float)
Salidas:
salarioBruto (float)
totalDeducciones (float)
salarioLíquido (float)
Restricciones:
horasLaboradas y horasExtra son
enteros.
horasLaboradas > 0.
horasExtra >=0
salarioPorHora y
salarioPorHoraExtra son float > 0.0"""
def calcularSalarioDeducciones():
    horasLaboradas = 0.0
    salarioPorHora = 0.0
    horasExtra = 0
    salarioPorHoraExtra = 0.0
    salarioBruto = 0.0
    totalDeducciones = 0.0
    salarioLiquido = 0.0

    print("Indique las horas laboradas: ")
    horasLaboradas = float(input())

    print("Indique el salario por hora: ")
    salarioPorHora = float(input())

    print("Indique las horas extra laboradas: ")
    horasExtra = float(input())

    print("Indique el salario por hora laborada: ")
    salarioPorHoraExtra = float(input())

    salarioBase = horasLaboradas * salarioPorHora
    salarioExtra = horasExtra * salarioPorHoraExtra
    salarioBruto = salarioBase + salarioExtra
    totalDeducciones = salarioBruto * 0.0934
    salarioLiquido = salarioBruto - totalDeducciones

    print("Monto de salario bruto ", salarioBruto)
    print("Monto de salario liquido", salarioLiquido)
    print("Monto de Deducciones", totalDeducciones)
calcularSalarioDeducciones()

#Reto 5
"""Entradas: 
annosVividos (int)

Salidas:
diasVividos (int)
semanasVividas (int)
mesesVividos (int)
horasVividos (int)

Restricciones:
annos vividos > 0
annos int"""

def calcularAnnosDeVidaEnTiempo():
    annosVividos = 0
    semanasVividas = 0
    mesesVividos = 0
    diasVividos = 0
    horasVividas = 0

    print ("Indique su edad en annos: ") 
    annosVividos = int(input())
    mesesVividos = annosVividos * 12
    semanasVividas = annosVividos * (4.34 * 12)
    diasVividos = annosVividos * 365
    horasVividas = annosVividos * 24 * 3654

    print("Annos Vividos", annosVividos)
    print("Meses Vividos", mesesVividos)
    print("Semanas Vividas",semanasVividas)
    print("Dias vividos", diasVividos)
    print("Horas Vividas", horasVividas)

calcularAnnosDeVidaEnTiempo()

#Reto 6
"""Entradas: 
tiempoDeLlamadaEnMinutos (float) 
costoPorMinuto (float)

Salidas:
costoDeLlamada (float)

Restricciones:
tiempo > 0 int
costoPorMinutos > 0 float
costoDeLlamada > 0 float"""

def calcularCostoDeLlamada():
    tiempoDeLlamadaEnMinutos = 0.0
    costoPorMinuto = 0.0
    costoDeLlamada = 0.0

    costoPorMinuto = 20 
    print("El costo de la llamada por minuto es de:" , costoPorMinuto)
    print("Cuantos minutos duro su llamada? ")
    tiempoDeLlamadaEnMinutos = float(input())
    
    costoDeLlamada = costoPorMinuto * tiempoDeLlamadaEnMinutos

    print ("El valor de su llamada es de: ", costoDeLlamada)

calcularCostoDeLlamada()
