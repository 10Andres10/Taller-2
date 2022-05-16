print("---------- Cuál -----------")
print("----------- es ------------")
print("---------  mayor ----------")

#input
a = int(input( "Digite el primer número: "))
b = int(input( "Digite el segundo número: "))
c = int(input( "Digite el tercer número: "))

#procesing
if a > b and b > c:
    msj = a
else:
    b > a and b > c
    msj = b

if c > a and c > b:
    msj = c

#output

print( "El número mayor es: " + str(msj))