# Importar las librerías necesarias
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir una función para dibujar un vector en 3D
def dibujar_vector(x, y, z):
    # Crear una figura y un eje 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d') #Se utiliza para crear un espacio de dibujo tridimensional (3D)

    # Dibujar el sistema de coordenadas en rojo (X), verde (Y) y azul (Z)
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='X') #primer conjunto de 0 es para indicar el origen 
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='Y') #segundo conjuto de numeros corresponde a (x,y,z)
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='Z') 

    # Dibujar el vector ingresado por el usuario en negro
    ax.quiver(0, 0, 0, x, y, z, color='black', label='Vector') # quiver trazar un vector

    # Etiquetas de los ejes y título del gráfico
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Sistema de Coordenadas 3D')   
    plt.show()

# Ingreso de coordenadas del vector por parte del usuario
x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))

# Dibujar el vector utilizando la función definida anteriormente
dibujar_vector(x, y, z)

