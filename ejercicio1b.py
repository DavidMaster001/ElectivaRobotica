#Ejercicio 1#
# usar la fórmula de la potencia eléctrica, que es el producto de la corriente y el voltaje. La fórmula es la siguiente:
#P=I×V
#Donde P es la potencia en vatios, I es la corriente en amperios y V es el voltaje en voltios.
#Para escribir un programa en Python que calcule la potencia, puedes seguir estos pasos:

#Pedir al usuario que ingrese el valor de la corriente y el voltaje usando la función input().
#Convertir los valores ingresados a números de tipo float usando la función float().
#Calcular la potencia usando la fórmula y asignar el resultado a una variable.
#Mostrar el resultado usando la función print().##



# Pedir al usuario que ingrese el valor de la corriente
I = float(input("Ingrese el valor de la corriente en amperios: "))

# Pedir al usuario que ingrese el valor del voltaje
V = float(input("Ingrese el valor del voltaje en voltios: "))

# Calcular la potencia usando la fórmula#
P = I * V

# Mostrar el resultado
print("La potencia que consume el circuito es", P, "vatios.")
