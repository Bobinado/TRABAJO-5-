#EJERCICIO 1:
"""
from redondear import redondear
numero=float(input("Ingresa un número decimal: "))
resultado=redondear(numero)
print(resultado)
"""
#EJERCICIO 2:
"""
from redondear import redondear
def suma(a,b):
    resultado=a+b
    print(f"Resultado:{resultado}")
    resultado=redondear(resultado)
    print(f"Resultado redondeado:{resultado}")

A=float(input("Num1: "))
B=float(input("Num2: "))
suma(A,B) 
"""
#EJERCICIO 3: 
"""
from datetime import datetime
fecha=datetime.today().date()
hora=datetime.now().time()
print(f"Fecha: {fecha}")
print(f"Hora: {hora}")
"""
#EJERCICIO 4:
"""
import random
numero=random.randrange(2,11,2)
print(numero)
"""
#EJERCICIO 5: 
"""
import random
def respuestas(respuesta):
    if respuesta==1:
        print("Es seguro que si")
    elif respuesta==2:
        print("Las chances son buenas")
    elif respuesta==3:
        print("Puedes contar con ello")
    elif respuesta==4:
        print("Pregúntame de nuevo más tarde")
    elif respuesta==5:
        print("Concéntrate y pregunta de nuevo")
    elif respuesta==6:
        print("No veo con claridad, intenta de nuevo")
    elif respuesta==7:
        print("Mi respuesta es no")
    elif respuesta==8:
        print("Mis fuentes me dicen que no")
while True:
    pregunta=input("Ingrese su pregunta: ")
    respuesta=random.randrange(1,8)
    respuestas(respuesta)
"""
#EJERCICIO 6:
"""
import time
inicio=time.time()

from redondear import redondear
numero=float(input("Ingresa un número decimal: "))
resultado=redondear(numero)
print(resultado)

final=time.time()
print(f"Tiempo de ejecución: {final-inicio}")
"""
#EJERCICIO 7:
"""
import random
numero=random.randrange(1,35)
papel=random.randrange(1,35)
print(f"Tu número es {numero}")
if numero==papel:
    print(f"Número ganador: {papel}, ¡felicidades!")
else:
    print(f"Número ganador: {papel}, que mala suerte")

"""
#EJERCICIO 8:
"""
from datetime import datetime
def dias():
    nacimiento=input("Fecha de naciminento (DD/MM/AAAA): ")
    nacimiento=datetime.strptime(nacimiento,'%d/%m/%Y')
    fecha=datetime.now()
    dias=fecha-nacimiento
    return (dias.days-1)
print(dias())
"""


