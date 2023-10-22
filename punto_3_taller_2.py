#funcion para convertir los 2 numeros en str
def espejo(numero1, numero2):
  str_numero1 = str(numero1)
  str_numero2 = str(numero2)
    
  #se comparan las listas con la otra invertida  
  if str_numero1 == str_numero2[::-1] and str_numero2 == str_numero1[::-1]:
    return True
  else:
    return False

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

#si se cumple la funcion espejo se imprime el resultado
if espejo(numero1, numero2):
  print(f"{numero1} y {numero2} son números espejos.")
else:
  print(f"{numero1} y {numero2} no son números espejos.")
