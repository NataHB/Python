'''
#ejercicio 1
Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
En caso de no introducir una opción válida, el programa informará de que no es correcta.

numero_1 = int(input('introduce el primer numero: '))
numero_2 = int(input('introduce el segundo numero: '))

print('1. Suma')
print('2. Resta')
print('3. Multiplicacion')
print('4. Salir')

opcion = int(input('elige una opcion: '))

if opcion == 1:
    print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')
elif opcion == 2:
    print(f'{numero_1} - {numero_2} = {numero_1 - numero_2}')
elif opcion == 3:
    print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
elif opcion == 4:
    print('Saliendo...')
else:
    print('Opcion no valida')
'''

'''
# ejercicio 2 
Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

 numero_impar = int(input('introduce un numero impar: '))
 while(numero_impar % 2 == 0):
     numero_impar = int(input('introduce un numero impar: '))
'''

'''
#ejercicio 3 
Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100:da mal el resultado

print(sum(range(0, 101, 2))) 

suma_impares = 0 
for i in range(101): 
     if i % 2 != 0: 
         suma_impares += i

print("La suma de todos los números impares desde 0 hasta 100 es:", suma_impares)
'''

'''
#ejercicio 4
Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.

cantidad = int(input('Cuantos numeros quieres introducir: '))
suma = 0
for i in range(cantidad):
    numero = int(input('Introduce un numero: '))
    suma += numero

print(f'La media aritmetica es: {suma /cantidad}')
'''
'''
#ejercicio 5
Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False).

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numero_entero = int(input('Introduce un numero del 0 al 9: '))
while numero_entero < 0 or numero_entero > 9:
    print('El numero no es correcto')
    numero_entero = int(input('Introduce un numero del 0 al 9: '))

if numero_entero in lista:
    print('El numero se encuentra en la lista')
'''

'''
#ejercicio 6
Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))

listas = {
    'lista0':  list(range(11)),
    'lista1':  list(range(-10, 1)),
    'lista2':  list(range(0, 21, 2)),
    'lista3':  list(range(-19, 0, 2)),
    'lista4':  list(range(0, 51, 5))
}
for i in listas:
    print (listas[i])
'''

'''
Realizar una función llamada año_bisiesto:

Recibirá un año por parámetro
Imprimirá “El año año es bisiesto” si el año es bisiesto
Imprimirá “El año año no es bisiesto” si el año no es bisiesto
Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

Información a tener en cuenta:

Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
'''

def anio_bisiesto(anio):
    while not anio.isdigit():
        anio = input('ingresa un numero valido: ')

    anio = int(anio)

    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
         print('El año es bisiesto')
    else:
         print('El año no es bisiesto')

anio_bisiesto(input('ingresa un anio: '))
