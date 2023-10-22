#funcion que reconoce los numeros repetidos con una lista vacia para almacenarlos
def elem_repetidos(lista):
  elem_unicos = set()
    
  for elemento in lista:
    if elemento in elem_unicos:
      return True
    elem_unicos.add(elemento)
    
  return False 

entrada = input("escriba una lista de elementos separados por espacios: ")

#convierte los numero de entrada en un lista
elementos = entrada.split()

#aplica la funcion
hay_repetidos = elem_repetidos(elementos)

#imprime los resultados segun la funcion
if hay_repetidos:
  print("La lista contiene elementos repetidos.")
else:
  print("La lista no contiene elementos repetidos.")
