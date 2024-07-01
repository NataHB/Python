#Actividad
lista_1 = [1, 2, 3]
#agregamos
lista_1.append(456789)
lista_1.append('hola mundo')

lista_2 = [4, 5, 6]
#agregamos
lista_2.append('hola y adios')

print(lista_1)
print(lista_2)

#elimina el ultimo
lista_3 = lista_1[:-1]
print(lista_3)

#elimina primero y ultimo
lista_4 = lista_2[1:-1]
print(lista_4)

#concatenamos
lista_5 = lista_3 + lista_4
print(lista_5)

#ordenar
lista_6 = sorted(lista_5)
print(lista_6)

#revertir
lista_7 = lista_6[::-1]
print(lista_7)

#suma los 3 numeros y agregalo al final
matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

nueva_matriz = []

for lista in matriz:
    suma = sum(lista)
    nueva_lista = lista + [suma]
    nueva_matriz.append(nueva_lista)

print(nueva_matriz)