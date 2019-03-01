mayores=0
cero=0
menores=0

for x in range(0,10):
    x=int(input("digite un numero"))
    if x==0:
            cero=cero + 1

    else:
        if x>0:
            mayores=mayores + 1

        else:
            menores=menores + 1

print("la cantidad de cero es: ", cero)
print("la cantidad de mayores es: ", mayores)
print("la cantidad de cero es: ", menores)
