print("---------- Tiempo de -----------")
print("---------- duración ------------")
print("-------- de una llamada --------")

#input
t = int(input("Digite la duración de la llamada: "))

#procesing
if t <= 3:
    t = 300

else:
    t = 300 + 50*(t-3)

#output

print( "El valor de la llamada es: " +str(t))