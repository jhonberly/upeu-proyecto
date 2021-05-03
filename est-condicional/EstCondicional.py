def estCondicional01():
 #Definir variables y otros
 print("Ejemplo estructura Condicional en Python")
 montoP=0
 #Datos de entrada
 cantidadX=int(input("Ingrese la cantidad de lapices:"))
 #Proceso
 if cantidadX>=1000:
  montoP=cantidadX*0.80
 else:
  montoP=cantidadX*0.90
 #Datos de salida
 print("El monto a pagar es:", montoP)
estCondicional01()
def bonoDocente():
  #definir Variables
  bonoObtenido=0.0
  #Datos de Endrada
  salarioMinimo=float(input("Ingrese el salario minimo:"))
  puntuacionObtenida=float(input("Ingrese la puntuación que ha obtenido:"))
  #Proceso
  if puntuacionObtenida<=100 and puntuacionObtenida>=0:
    bonoObtenido=salarioMinimo
  elif puntuacionObtenida >=101 and puntuacionObtenida<=150:
    bonoObtenido=salarioMinimo*2
  elif puntuacionObtenida>150:
    bonoObtenido=salarioMinimo*3  
  #Datos de salida
  print("El docente obtendra un bono de:", bonoObtenido )

#estCondicional02()
#estCondicional01()
bonoDocente()