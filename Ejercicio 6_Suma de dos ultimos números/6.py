#Construir un programa que lea un número entero 
#y que determine si el resultado de sumar sus dos últimos
#dígitos es un número de 1 dígito.

print("---------- SUMA DE 2 -------------")
print("----------- ULTIMOS --------------")
print("----------- DIGITOS --------------")

a = input(" Escriba un número de 4 dígitos: ")
a = int(a)

b = int(a % 10)
c = int(a / 10)
d = int(b % 10)

Z = int(b + d)

if Z <= 9 and Z >= 1:
    print(" La suma de los dos ultimos dígitos es " + str(Z) + " y es un número de 1 dígito. ")

else:
    print(" La suma de los dos ultimos dígitos es " + str(Z) + " y NO es un número de 1 dígito. ")