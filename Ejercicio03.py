#Entrada
a = int(input("Ingrese numeros positivo: "))

#Proceso

if a >= 1000:
    print("El primer digito del numero es", str(a/1000))
elif a >= 100:
    print("El primer digito del numero es", str(a/100))
elif a >= 10:
    print("El primer digito del numero es", str(a/10))
if a >= 1000:
    print("El numero es de un digito")