#funcion para convertir los int en str y una lista vacia
def lista(numero):
  num_str = str(numero)
  lista = []
    
  #devuelve el valor a int y lo agrega a la lista
  for digito in num_str:
    lista.append(int(digito))  
  return lista

numero = int(input("Ingresa un número entero: "))

#almacena el resultado de la funcion
resultado = lista(numero)

print("los digitos del numero son:", resultado)
