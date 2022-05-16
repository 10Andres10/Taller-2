print("------- Positivo de -----")
print("-----------  4 ----------")
print("--------- Dígitos -------")
print("----- ¿Par ó Impar? -----")

#input
A = input (" Escriba un número de 4 cifras: ")
A = int (A)

#procesing
D = A % 10
Z = D % 2
if Z == 0:
    R = ( "El número " + str (A) + " es par. ")

else:
    R = ( "El número " + str (A) + " es impar. " )

#output
print (R)