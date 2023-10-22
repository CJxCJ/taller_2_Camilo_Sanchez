#RECURSIVA

#funcion que define el mcd usando recurcion
def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

#funcion para el mcm con el retorno de la funcion de mcd usando recurcion
def mcm(a, b):
  return (a * b) // mcd(a, b)

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

#imprime la funcion mcm 
resultado = mcm(num1, num2)
print(f"El mcm de {num1} y {num2} es {resultado}")
