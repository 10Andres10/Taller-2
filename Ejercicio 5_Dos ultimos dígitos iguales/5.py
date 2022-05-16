#Construir un programa que lea un número entero y que determine si sus dos últimos dígitos son iguales.

print("----------------------------")
print("----- Números iguales-------")
print("----------------------------")

q = input(" Escriba un número ")
q = int(q)

a = int(q % 10)
b = int(q / 10)
c = int(b % 10)

if a == c:
    print(" Los dos ultimos números son iguales ")
else:
    print(" Los dos ultimos números no son iguales ")