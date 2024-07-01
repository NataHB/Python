# Desafio string
cadena_1 = "versátil"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programación"
print(cadena_2, cadena_3, cadena_4, cadena_1)

# Desafio numeros
partidos_ganados = int(input('cuantos ganaste?'))
partidos_empatados = int(input('cuantos empataste?'))
partidos_perdidos = int(input('cuantos perdiste?'))
puntaje_ganados = partidos_ganados*3
puntaje_empatados = partidos_empatados*1
puntaje_perdidos = partidos_perdidos*0
print((puntaje_empatados + puntaje_ganados + puntaje_perdidos)*0.20)

# Desafio Slicing
cadena = "acitametaM ,5.8 ,otipeP ordeP"
cadena_volteada = cadena[::-1]
nombre_alumno = cadena_volteada[0:12]
nota_alumno = cadena_volteada[14:17]
materia_alumno = cadena_volteada[19:29]
print(nombre_alumno, 'ha sacado un', nota_alumno, 'en', materia_alumno)

# Primer desafio
nota_1 = int(input('decime tu primer nota'))
nota_2 = int(input('decime tu segunda nota'))
nota_3 = int(input('decime tu tercer nota'))
nota_final = ((nota_1*0.20) + (nota_2*0.30) + (nota_3*0.50))
print('la nota final es', nota_final)


