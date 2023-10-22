#funcion que define cuales son las vocales
def vocales(cadena):
  vocales = "a e i o u A E I O U"
  conteo = 0
  #hace que la funcion se aplique por toda la lista
  for letra in cadena:
    if letra in vocales:
      conteo += 1
    #si tiene mas de 2 vocales regresa true  
    if conteo >= 2:
      return True
  return False

#pedir la lista
entrada = input("escriba cadenas/palabras separadas por espacios: ")

#convierte los datos de entrada en una lista de cadenas.
cadenas = entrada.split()

#imprime la respuesta de todas las cadenas/palabras que cumplan la funcion
print("Cadenas con dos o más vocales en la lista:")
for cadena in cadenas:
  if vocales(cadena):
    print(cadena)
