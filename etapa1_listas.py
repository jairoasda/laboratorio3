lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Lista original:")
for numero in lista:
    print(numero)

nuevo = int(input("Ingresa el nuevo valor para el tercer elemento: "))
lista[2] = nuevo

print("Lista modificada:")
for numero in lista:
    print(numero)

buscar = int(input("Ingresa un número para buscar: "))

if buscar in lista:
    print("El número existe en la lista.")
else:
    print("El número no existe.")