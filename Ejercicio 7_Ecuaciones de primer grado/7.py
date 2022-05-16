print("------ Ecuaciones ------")
print("------ de Primer -------")
print("-------- Grado----------")

A = int(input(" Ingrese el valor de a: "))
B = int(input(" Ingrese el valor de b: "))

if A !=0 and B != 0:
    X = int((-1*B)/A)
    print(" La solución de la ecuación es " + str(X))
else:
    print(" Indeterminada.Ingrese valores diferentes a 0 ")