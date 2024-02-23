print("Seleccione el tipo de robot para el que desea conocer el tipo y el número de articulaciones:")
print("1. Robot Cilíndrico")
print("2. Robot Cartesiano")
print("3. Robot Esférico")
print("4. Salir")

opcion = int(input("Ingrese el número de la opción: "))

if opcion == 1:
  # Mostrar la información del robot cilíndrico
  print("El robot cilíndrico tiene 3 articulaciones: una rotacional y dos lineales.")
  print("Su movimiento se basa en coordenadas cilíndricas: ángulo, radio y altura.")
elif opcion == 2:
  # Mostrar la información del robot cartesiano
  print("El robot cartesiano tiene 3 articulaciones lineales, perpendiculares entre sí.")
  print("Su movimiento se basa en coordenadas cartesianas: x, y, z.")
elif opcion == 3:
  # Mostrar la información del robot esférico
  print("El robot esférico tiene 3 articulaciones: una rotacional y dos angulares.")
  print("Su movimiento se basa en coordenadas esféricas: ángulo, inclinación y radio.")
elif opcion == 4:
  # Terminar el programa
  print("Gracias por usar este programa.")
else:
  # Mostrar un mensaje de error si la opción no es válida
  print("Opción inválida. Intente de nuevo.")