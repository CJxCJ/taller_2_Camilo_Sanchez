#funcion definiendo los multiplos de 3 previamente
def multiplo_de_tres(numero):
  suma = sum(int(digito) for digito in str(numero))
  return suma in {0, 3, 6, 9}

#funcion para hallar los multplos de 3 (ya definidos) en la lista
def encontrar_multiplos(lista):
  multiplos = [num for num in lista if multiplo_de_tres(num)]
  return multiplos

#solitar la lista 
lista = [int(x) for x in input("Ingresa una lista de números enteros separados por espacios: ").split()]

#aplicar la segunda funcion
multiplos = encontrar_multiplos(lista)

#imprimir los múltiplos de 3 en la lista
print("Los múltiplos de 3 en la lista son:", multiplos)