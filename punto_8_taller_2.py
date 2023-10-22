#funcion para reconocer los elementos de la 1ra lista que no estan en la 2da
def elementos(lista1, lista2):
  return [elemento for elemento in lista1 if elemento not in lista2]

#pedir las 2 listas
lista1 = input("escriba la primera lista de elementos separados por espacios: ").split()
lista2 = input("escriba la segunda lista de elementos separados por espacios: ").split()

#se aplica la funcion
no_comunes = elementos(lista1, lista2)

#imprime los elementos no comunes
print("Los lementos de la primera lista que no están en la segunda lista son:")
for elemento in no_comunes:
  print(elemento)
