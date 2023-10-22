#funcion que crea una lista vacia y analiza si son o no multiplos de 3 los datos
def multiplos_de_tres(lista):
    multiplos = []
    for num in lista:
      if num % 3 == 0:
        multiplos.append(num)
    return multiplos

#pedir los numeros separados por espacio y hacer cada valor un dato independiente
entrada = input("Ingresa los valores de la lista separados por espacios: ")
valores = [int(valor) for valor in entrada.split()]

#usa la funcion en la lista creada
multiplos = multiplos_de_tres(valores)

print("Los múltiplos de 3 en la lista son:", multiplos)
