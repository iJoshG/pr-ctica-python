#Imprimir tu nombre
nombre = input("Introduce tu Nombre: ")
print(f"Hola! {nombre}")

#Número Entero
edad = 25
#Número Flotante - decimales
altura = 1.75
#Convertir flotante
edadString = str(edad)
print(edad + edad)
print(edadString + edadString)

print(type(edadString))

tuEdad = input("Introduce tu Edad: ")
tuEdad = int(tuEdad)

#Estructura de Control if
if tuEdad >= 18 and tuEdad < 100:
    print("Eres Legal!")
elif tuEdad >= 100:
    print("Alm Eres GOD :o")
else:
    print("Eres Ilegal :(")

#Esto imprime todos los números en rango 0 a -10
for i in range (0, 10):
    print(i)