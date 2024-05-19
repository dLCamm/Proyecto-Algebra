from numpy import matrix, zeros, size
from numpy.linalg import det, inv
import numpy as np
import random


g = int(input('Ingrese el numero de columnas de su cifrado'))

matriz = []
llave =[]
for i in range(3):
    fila = []
    for j in range(g):
        valor = float(input(f"Ingrese el elemento [{i+1},{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

for i in range(3):
    ll = []
    for j in range(3):
     
      ll.append(random.randint(1, 20))
  
    llave.append(ll)


cod = np.array(matriz)
key = np.array(llave)
print('Esta es su llave')
print(key)

print('La inversa es')
inversa = np.linalg.inv(key)
print(inversa)
print('')
print('Determinante')
det = det(key)
print(det)
print('')

print('Cifrado')
            
div = np.dot(key,cod)
print(div)

print('')
print('Decifrado')
des =  np.dot(inversa,div)
print(des)
