lista = [10, 20, 30]
while True:

    print("\n--- MENÚ ---")
    print("1. Insertar")
    print("2. Eliminar")
    print("3. Buscar")
    print("4. Mostrar")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        numero = int(input("Ingresa el número: "))
        lista.append(numero)
        print("Número insertado.")

    elif opcion == 2:
        posicion = int(input("Ingresa la posición: "))
        if 0 <= posicion < len(lista):
            lista.pop(posicion)
            print("Elemento eliminado.")
        else:
            print("Posición inválida.")

    elif opcion == 3:
        numero = int(input("Número a buscar: "))
        if numero in lista:
            print("Se encuentra en la posición:", lista.index(numero))
        else:
            print("No se encontró.")

    elif opcion == 4:
        print("Lista:", lista)

    elif opcion == 5:
        print("Programa terminado.")
        break

    else:
        print("Opción inválida.")