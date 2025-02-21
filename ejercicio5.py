def bubble_sort(lista):
    numero = len(lista)
    contador=0
    for i in range(numero):
        for j in range(numero-1-i):
            contador+=1
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print(contador)
    return lista

lista = [8,6,1,4,44,9,0,22]
print(bubble_sort(lista))
