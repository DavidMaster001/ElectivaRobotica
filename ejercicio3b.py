#Ejercicio 3 #------------------------------------------------------------------

def volumen_prisma(base, altura):
  # La fórmula del volumen del prisma es base por altura
  return base * altura

def volumen_cono_truncado(radio_mayor, radio_menor, altura):
  # La fórmula del volumen del cono truncado es (1/3) por pi por altura por (radio mayor al cuadrado más radio menor al cuadrado más radio mayor por radio menor)
  return (1/3) * math.pi * altura * (radio_mayor * 2 + radio_menor * 2 + radio_mayor * radio_menor)

print("Seleccione el tipo de sólido para el que desea calcular el volumen:")
print("1. Prisma")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro")
print("5. Salir")

opcion = int(input("Ingrese el número de la opción: "))

if opcion == 1:
  # Pedir al usuario que ingrese los valores de la base y la altura del prisma
  #base = float(input("Ingrese el valor de la base del prisma: "))
  altura = float(input("Ingrese el valor de la altura del prisma: "))
  # Llamar a la función volumen_prisma y asignar el resultado a una variable
  volumen = volumen_prisma(base, altura)
  # Mostrar el resultado al usuario
  print("El volumen del prisma es:", volumen)
elif opcion == 2:
  base = float(input("Ingrese el valor de la base del Pirámide: "))
  altura = float(input("Ingrese el valor de la altura del Pirámide: "))
  # Llamar a la función volumen_prisma y asignar el resultado a una variable
  volumen = volumen_prisma(base, altura)
   # Mostrar el resultado al usuario
  print("El volumen del Pirámide es:", volumen)
  
elif opcion == 3:
  base = float(input("Ingrese el valor de la base del Cono truncado: "))
  altura = float(input("Ingrese el valor de la altura del Cono truncado: "))
  # Llamar a la función volumen_prisma y asignar el resultado a una variable
  volumen = volumen_prisma(base, altura)
   # Mostrar el resultado al usuario
  print("El volumen del Cono truncado es:", volumen)
  ...
elif opcion == 4:
  base = float(input("Ingrese el valor de la base del Cilindro: "))
  altura = float(input("Ingrese el valor de la altura del Cilindro: "))
  # Llamar a la función volumen_prisma y asignar el resultado a una variable
  volumen = volumen_prisma(base, altura)
   # Mostrar el resultado al usuario
  print("El volumen del Cilindro es:", volumen)
  # Hacer lo mismo para el cilindro
  ...
elif opcion == 5:
  # Terminar el programa
  print("Gracias por usar este programa.")

else:
  # Mostrar un mensaje de error si la opción no es válida
  print("Opción inválida. Intente de nuevo.")
