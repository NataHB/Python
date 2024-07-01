'''
Crear un conjunto en Python que posea los siguientes elementos:
Países: Inglaterra, USA, México.
Posteriormente agrega nuestro set de países, los elementos de: Islandia, Italia, Argentina y Portugal, USA
Elimina a los países: Chile e Italia
'''

paises = {'Inglaterra', 'USA', 'Mexico'}
paises.update({'Islandia', 'Italia', 'Argentina', 'Portugal', 'USA'})
paises.remove('Chile')
paises.remove('Italia')
print(paises)

'''
Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo muestre por pantalla:
Ejemplo del output solicitado: 
Juan tiene 25 años, y vive en Carrera 7 - Bogotá
''' 

datos = {
    'usuario': input('Cual es tu nombre?'),
    'edad': int(input('Cuantos años tienes?')),
    'ciudad': input('Cual es tu ciudad?')
}

print(f'{datos["usuario"]} tiene {datos["edad"]} años, y vive en {datos["ciudad"]}')
