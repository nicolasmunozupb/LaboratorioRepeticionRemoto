pares=0
for x in range(0,99999999999999999999999999999999999999999999):
        x=int(input("digite un numero"))

        if x % 2 ==0:
                pares = pares + 1
        else:
                break
print("el programa se detuvo por el ingreso de un numero impar; u la cantidd de numeros pares fue:", pares)
