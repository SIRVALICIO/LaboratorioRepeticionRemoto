ContPares=0
for x in range(0,1888888):
    a=int(input("numero: "))
    if a%2==0:
        ContPares+=1
    else:
        if a%2!=0:
            break
print("la cantidad de numeros pares son: ",ContPares)


