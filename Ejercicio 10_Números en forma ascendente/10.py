print(" / / / / NÚMEROS / /  / / / /")
print(" / / / / EN FORMA / / / / / /")
print(" / / / / ASCENDENTE / / / / /")

x=int(input("Digite el primer número: "))
y=int(input("Digite el segundo número: "))
z=int(input("Digite el tercer número: "))

if x>y:
    if x>z:
        if z>y:
            print("El orden ascendente es" + str(y) + str(z) + str(x))
        else:
            print("El orden ascendente es" + str(z) + str(y) + str(x))
    else:
        print("El orden ascendente es" + str(y) + str(x) + str(z))
else:
    if y>z:
        if z>x:
            print("El orden ascendente es" + str(x) + str(z) + str(y))
        else:
            print("El orden ascendente es" + str(z) + str(x) + str(y))
    else:
        print("El orden ascendente es" + str(x) + str(y) + str(z))