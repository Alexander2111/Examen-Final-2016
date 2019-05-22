n = [4,12,87,69,3,6,5,65,44,62,53,98]
for recorrido in range(1,len(n)):
    for posicion in range(len(n)-recorrido):
        if n[posicion] > n[posicion + 1]:
            temp = n[posicion]
            n[posicion] = n[posicion + 1]
            n[posicion + 1] = temp
print(n)