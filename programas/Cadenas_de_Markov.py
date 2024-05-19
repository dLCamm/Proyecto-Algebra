import numpy as np
from numpy import matrix
m = []
p = []

columnas = int(input('Ingrese el numero de columnas de su cifrado: '))
filas = int(input('Ingrese el numero de filas de su cifrado: '))

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f"Ingrese el elemento [{i+1},{j+1}]: "))
        fila.append(valor)
    m.append(fila)

print('')

for i in range(filas):
    prob = float(input(f'Ingrese la probabilidad {i+1}: '))
    p.append(prob)

matriz = np.array(m)
print(p)
print('')

y = np.transpose(matriz)
print("Transpuesta \n", y)
print('')

print("multiplicacion:", np.dot(y, p))
print('')

num = int(input("Ingrese el periodo: "))
for i in range(1, num + 1):
    mult = np.dot(y, p)
    p = mult
print('El resultado es:')
print(mult)








