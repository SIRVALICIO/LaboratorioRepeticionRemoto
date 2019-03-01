contMayores=0
contMenores=0
contIguales=0

for x in range(0,5):
    a = int(input("Numero Deseado a comparar: "))
    if a>0:
        contMayores+=1
    else:
        if a==0:
            contMenores+=1
        else:
            contIguales+=1

print("Los numeros mayores son: ", contMayores)
print("la cantidad de numeros menores son: ", contMenores)
print("la cantidad de 0 son: ", contIguales)