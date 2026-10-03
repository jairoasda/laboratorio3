matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        numero = int(input(f"Ingresa el número [{i}][{j}]: "))
        fila.append(numero)
    matriz.append(fila)
    print("Matriz:")

for fila in matriz:
    print(fila)
    suma = 0

for i in range(3):
    for j in range(3):
        suma += matriz[i][j]

print("Suma total:", suma)