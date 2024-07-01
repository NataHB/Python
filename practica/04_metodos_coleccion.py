'''A partir de una lista realizar las siguientes tareas sin modificar la lista original:
Borrar los elementos duplicados
Ordenar la lista de mayor a menor
Eliminar todos los números impares (  for ---- if (%2==1) ---- pop, remove   )
Realizar una suma de todos los números que quedan (sum(lista))
Añadir como primer elemento de la lista la suma realizada insert(0, suma)
Devolver la lista modificada
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista
'''
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

#Borrar los elementos duplicados
lista =set(lista)

#Ordenar la lista de mayor a menor
lista =sorted( lista, reverse=True )

#Eliminar todos los números impares (  for ---- if (%2==1) ---- pop, remove   )
for i in lista:
    if 1%2==1:
        lista.remove(i)

#Realizar una suma de todos los números que quedan (sum(lista))
sum(lista)

#Añadir como primer elemento de la lista la suma realizada insert(0, suma)
lista.insert(0,sum(lista))

print(lista)