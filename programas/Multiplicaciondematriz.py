import numpy as np
Matriz1 = []
Matriz2 = []

filas1 = int(input('Ingrese el numero de filas para la matriz 1: '))
columnas1 = int(input('Ingrese el numero de columnas para la matriz 1: '))

filas2 = int(input('Ingrese el numero de filas para la matriz 2: '))
columnas2 = int(input('Ingrese el numero de columnas para la matriz 2: '))

if columnas1 == filas2:
    for fila in range(filas1): #
        Matriz1.append([])
        for columna in range(columnas1):
            Matriz1[fila].append(columna)

    for fila in range(filas1):
        for columna in range(columnas1):
            Matriz1[fila][columna] = int(input('Ingrese los digitos en orden: '))

    print()
    mat1= np.array(Matriz1)
    print('Esta es su primera matriz')
    print(mat1)
    print('Ahora la segunda matriz')
    print()

    for fila in range(filas2):
        Matriz2.append([])
        for columna in range(columnas2):
            Matriz2[fila].append(columna)

    for fila in range(filas2):
        for columna in range(columnas2):
            Matriz2[fila][columna] = int(input('Ingrese los digitos en orden: '))
    print()
    mat2 = np.array(Matriz2)
    print(' Esta es su segunda matriz')
    print(mat2)
    print()


    print('El resultado es:')
    print(mat1 @ mat2)
    
else:
    print('Multiplicacion no valida')