def suma_pares():
    lista=[1,2,3,4,5,6]
    suma = 0
    for i in lista:
        if i % 2 == 0:
            suma += i
    return suma

print(suma_pares())    