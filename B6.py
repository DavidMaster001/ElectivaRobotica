# Inicializar la respuesta del usuario
respuesta = ""

# Crear un bucle while que se ejecute mientras la respuesta no sea "No"
while respuesta != "No":
  #Pedir al usuario que ingrese su respuesta
  respuesta = input("¿Desea continuar Si/No? ")
  # Si la respuesta es "No", salir del bucle
  if respuesta == "No":
    break
  # Si no, volver al inicio del bucle
  else:
    continue

# Mostrar un mensaje al finalizar el bucle
print("Gracias por usar este programa.")