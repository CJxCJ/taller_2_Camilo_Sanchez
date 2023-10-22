#funcion que convuierte el int en un str
def lista(numero):
  num_str = str(numero)
    
    #separa el numero donde se encuntre el "." para separar la parte entera de la decimal
  partes = num_str.split(".")
    
  entero = partes[0]
  decimal = partes[1] if len(partes) > 1 else "0"
    
  #empieza la lista vacia para ir almacenando los int
  lista_entera = [int(digito) for digito in entero]
  lista_decimal = [int(digito) for digito in decimal]
    
  return lista_entera, lista_decimal

numero = float(input("Ingresa un número flotante: "))

#almacena el resultado de la funcion
lista_entera, lista_decimal = lista(numero)

print("Los digitos de la parte entera es:", lista_entera)
print("Los digitos de la parte decimal es:", lista_decimal)

