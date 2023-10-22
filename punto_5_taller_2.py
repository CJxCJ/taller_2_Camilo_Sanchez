#ITERATIBA

#funcion que define el mcd
def mcd(a, b):
  while b:
    a, b = b, a % b
  return a

#funcion para el mcm con el retorno de la funcion de mcd 
def mcm(a, b):
  return (a * b) // mcd(a, b)

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

#imprime la funcion mcm 
resultado = mcm(num1, num2)
print(f"El mcm de {num1} y {num2} es {resultado}")
