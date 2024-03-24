# Importar las librerías necesarias
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir una función para dibujar un vector en 3D
def dibujar_vector(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='X')
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='Y')
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='Z')
    ax.quiver(0, 0, 0, x, y, z, color='black', label='Vector')
    
    # Establecer los límites de la gráfica
    lim = max(abs(x), abs(y), abs(z))
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)

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

