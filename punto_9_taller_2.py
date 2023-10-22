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
