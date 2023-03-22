"""Ejercicio 6 Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

cant_materias = int(input('Ingrese la cantidad de materias: ')) 


if cant_materias == 2:
    print('Ingrese las materias: ')
    materia_0 = str(input())
    materia_1 = str(input())
    materias = list([materia_0, materia_1])
elif cant_materias == 3:        
    print('Ingrese las materias: ')
    materia_0 = str(input())
    materia_1 = str(input())
    materia_2 = str(input())
    materias = list([materia_0, materia_1, materia_2])
elif cant_materias == 4:        
    print('Ingrese las materias: ')
    materia_0 = str(input())
    materia_1 = str(input())
    materia_2 = str(input())
    materia_3 = str(input())
    materias = list([materia_0,materia_1,materia_2,materia_3])

notas = []

for materia in range(len(materias)):
    print('Ingrese tu nota en ', materias[materia],': ')
    nota = int(input())
    if nota < 4:
        notas.append(nota)


for i in range(len(notas)): 
    print('Tu nota en',materias[i], 'es de',notas[i],'\nDebes repetir la materia.')








