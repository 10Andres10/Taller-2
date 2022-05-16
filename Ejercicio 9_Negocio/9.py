print("- - - - - - -  - - - - ")
print("- - - - NEGOCIO - - - -")
print("- - - - - - - - - - - -")

print("Tipos de clientes: G, A")
CLIENTE = (input (" Digite el tipo de cliente: "))
B = float(input(" Digite el valor de la compra: "))


if CLIENTE == "G":
    d = float(B * 0.15)
    c = float(B - d)
    print(" El descuento para el Cliente General es de " + str(d) + " y el total a pagar es " + str(c))

    r = float(B * 0.10)
    p = float(B + r)
    print("El recargo para el Cliente General es de " + str(r) + " y el total a pagar es " + str(p))

elif CLIENTE == "A":
    d = float(B * 0.20)
    c = float(B - d)
    print("El descuento para el Cliente Afiliado es de " + str(d) + " y el total a pagar es " + str(c))

    r = float(B * 0.05)
    p = float(B + r)
    print("El recargo para el Cliente General es de " + str(r) + " y el total a pagar es " + str(p))

else:
    print(" Seleccione el tipo de cliente válido ")
