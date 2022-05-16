print("-------- Raices de ----------")
print("-------- Ecuaciones ---------")
print("----- en segundo grado ------")

A = int(input(" Ingrese el valor a: "))
B = int(input(" Ingrese el valor b: "))
C = int(input(" Ingrese el valor c: "))

Z = float(((B**2)-(4*A*C))**(1/2))

if Z < 0:
    print(" La solución de la raíz no existe en los Números Reales. ")
else:
    X1 = float((-B+Z)/(2*A))
    X2 = float((-B-Z)/(2*A))

print(" Las posibles soluciones de la ecuación son " + +str(X1) + " y " + str(X2) + " y el valor de la raíz es " + str(Z))