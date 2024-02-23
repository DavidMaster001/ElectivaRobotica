# Importar el módulo random
import random

# Pedir al usuario que ingrese el valor de X
X = int(input("Ingrese la cantidad de números aleatorios que desea obtener: "))

# Pedir al usuario que ingrese el valor del límite inferior del rango
limite_inferior = int(input("Ingrese el valor del límite inferior del rango: "))

# Pedir al usuario que ingrese el valor del límite superior del rango
limite_superior = int(input("Ingrese el valor del límite superior del rango: "))

# Crear una lista vacía para almacenar los números aleatorios
numeros_aleatorios = []

# Usar un bucle for que se repita X veces
for i in range(X):
  # Generar un número aleatorio usando la función randint()
  numero_aleatorio = random.randint(limite_inferior, limite_superior)
  # Agregar el número aleatorio a la lista
  numeros_aleatorios.append(numero_aleatorio) #Se utiliza para agregar un elemento al final de una lista

# Mostrar la lista con los números aleatorios
print("Los números aleatorios generados son:", numeros_aleatorios)
