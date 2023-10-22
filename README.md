# Taller 2 - CodeHouse

![logo_codehouse|100](https://github.com/CJxCJ/Taller_1_Camilo_Sanchez/assets/115903431/0617e276-9955-4f84-bb66-9a740f355b0f)

## Camilo Jose Sanchez Vilamar

## Punto 1:
Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).

## SOLUCION

````python
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

````

## Punto 2:
Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.

## SOLUCION

````python
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


````

## Punto 3:
Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

## SOLUCION

````python
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

````

## Punto 4:
Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.

## SOLUCION

````python
import math

#función para la aproximacion de coseno
def aprox_coseno(x, n):
  aprox = 0

  for i in range(n):
    termino = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    aprox += termino

  valor = math.cos(x)
  dif = abs(valor - aprox)

  return aprox, dif

#funcion para obtener el numero de terminos necesarios para obtener error
def term_necesarios(x, error_max):
  n = 0
  error = error_max + 1
  while error > error_max:
    n += 1
    aprox, _ = aprox_coseno(x, n)
    error = abs(math.cos(x) - aprox)
  return n

x = float(input("Ingresa el valor de x: "))

#errores deseados
errores_deseados = [0.1, 1, 10]

#se imprime el error con el porcentaje en fraccion 
for error_per in errores_deseados:
  error_max = error_per / 100  
  n_max = term_necesarios(x, error_max)
  aprox, dif = aprox_coseno(x, n_max)
  print(f"Para x = {x}, se necesita un mínimo de {n_max} términos para obtener un error del {error_per}% o menos.")
  print(f"Aproximación de cos({x}) con {n_max} términos: {aprox:.7f}")
  print(f"Diferencia con el valor real: {dif:.4f}")
  print()

````

## Punto 5.A:
Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.

## SOLUCION
````python
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

````

## Punto 5.B:

## SOLUCION

````python
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

````

## Punto 6:
Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in.

## SOLUCION

````python
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

````

## Punto 7:
Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

## SOLUCION

````python
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

````

## Punto 8:
Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. 

## SOLUCION

````python
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

````

## Punto 9:
 Resolver el punto 7 del [taller 1](https://github.com/fegonzalez7/pdc_unal_clase8) usando operaciones con vectores.

## SOLUCION

````python
#funciones de todas las operaciones que se requieren
def calcular_promedio(v, w, x, y, z):
  return (v + w + x + y + z) / 5

def calcular_mediana(v, w, x, y, z):
  lista = [v, w, x, y, z]
  lista.sort()
  return lista[2]

def calcular_promedio_multiplicativo(v, w, x, y, z):
  return (v * w * x * y * z) ** (1/5)

def orden_ascendente(v, w, x, y, z):
  lista = [v, w, x, y, z]
  lista.sort()
  return lista

def orden_descendente(v, w, x, y, z):
  lista = [v, w, x, y, z]
  lista.sort(reverse=True)
  return lista

def calcular_potencia_mayor_menor(v, w, x, y, z):
  return max(v, w, x, y, z) ** min(v, w, x, y, z)

def calcular_raiz_cubica_menor(v, w, x, y, z):
  return min(v, w, x, y, z) ** (1/3)

#se piden los 5 datos necesarios para calcular las funciones
v = float(input("Ingrese el primer número: "))
w = float(input("Ingrese el segundo número: "))
x = float(input("Ingrese el tercer número: "))
y = float(input("Ingrese el cuarto número: "))
z = float(input("Ingrese el quinto número: "))

#definen variables de las funciones
prom = calcular_promedio(v, w, x, y, z)
medi = calcular_mediana(v, w, x, y, z)
geo = calcular_promedio_multiplicativo(v, w, x, y, z)
orde = orden_ascendente(v, w, x, y, z)
edro = orden_descendente(v, w, x, y, z)
pot = calcular_potencia_mayor_menor(v, w, x, y, z)
cub = calcular_raiz_cubica_menor(v, w, x, y, z)

#imprime los resultados
print(f"{prom:.5f} es el promedio")
print(f"{medi} es la mediana")
print(f"{geo:.5f} es el promedio multiplicativo")
print(f"{orde} es el orden ascendente")
print(f"{edro} es el orden descendente")
print(f"{pot} es la potencia del mayor elevado por el menor")
print(f"{cub:.5f} es la raíz cúbica del menor")

````

## Punto 10.A:
Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser **retornada** por la función. Implemente la perspectiva de un *patrón de acumulación* y también de *comprensión de listas*. **Desafío:** Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). **Pista:** Un número es multiplo de 3 si la suma de sus dígitos también lo es

## SOLUCION

````python
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

#resultado
print("Los múltiplos de 3 en la lista son:", multiplos_de_tres)

````

## Punto 10.B:

## SOLUCION

````python
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
````
