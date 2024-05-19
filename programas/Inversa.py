import numpy as np

f = int(input('Ingrese el numero de filas y columnas (La matriz es cuadada)'))

matriz = []
for i in range(f):
    fila = []
    for j in range(f):
        valor = float(input(f"Ingrese el elemento [{i+1},{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

l = np.array(matriz)

print('')
print('Matriz')
print(l)
print('')

print('Matiz Inversa')
inversa = np.linalg.inv(l)
print(inversa)

