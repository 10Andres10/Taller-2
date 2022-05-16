print("----------- ¿Es un -----------")
print("------ número positivo -------")
print("-------- de 4 dígitos? -------")

x = int ( input ( " Digite un número " ) )

if x >= 1000 and x <= 9999:
    print ( " Si es un número positivo de 4 dígitos " )

else:
    print ( " Error, Digite un número válido" )