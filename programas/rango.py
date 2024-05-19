import numpy as np
def gauss():
    filascolumnas = int(input('Ingrese el numero de filas/columnas: '))
    matriz = []
    for i in range(filascolumnas):
        fila = []
        for j in range(filascolumnas):
            valor = float(input(f"Ingrese el elemento [{i},{j}]: "))
            fila.append(valor)
        matriz.append(fila)

    print('')
    pivot = matriz[0]

    for eq in range(0, len(matriz)):
        pivot = matriz[eq]
        for x in range(eq + 1, len(matriz)):
            multiplicador1 = pivot[eq] * (1 if pivot[eq] > 0 else -1)
            multiplicador2 = (matriz[x][eq] * (1 if matriz[x][eq] > 0 else -1)) * (
                1 if matriz[x][eq] * pivot[eq] < 0 else -1)
            for y in range(len(matriz[x])):
                matriz[x][y] *= multiplicador1
                sumando = pivot[y] * multiplicador2
                matriz[x][y] += sumando

    # Imprimir la matriz resultante

    l = np.array(matriz)
    print('Matriz Inicial')
    print(l)
    print('')
    def eliminar_filas_ceros(x):
 
        filas_sin_ceros = x[~np.all(x == 0, axis=1), :]
        return filas_sin_ceros
    
    sinceros = eliminar_filas_ceros(l)

    print("\nMatriz resultante:")
    print(sinceros)
    print('')
    print(f'El rango de la matriz es de: {len(sinceros)}')
    

gauss()
