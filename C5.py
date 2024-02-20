import matplotlib.pyplot as plt
import numpy as np

# Crear figura y ejes
fig, ax = plt.subplots()

# Configurar tamaño de la figura
fig.set_size_inches(6, 6)

# Dibujar el nombre "David"
# Línea recta D
ax.plot([0, 1], [1, 1], 'b')
ax.plot([0, 0], [0, 2], 'b')
ax.plot([0, 0.5], [0, 0], 'b')
ax.plot([0.5, 0.5], [0, 1], 'b')
# Línea recta A
ax.plot([1, 1], [0, 2], 'b')
ax.plot([1, 1.5], [2, 1], 'b')
ax.plot([1.5, 2], [1, 2], 'b')
# Línea recta V
ax.plot([2, 2.25], [0, 2], 'b')
ax.plot([2.25, 2.5], [2, 0], 'b')
# Línea recta I
ax.plot([2.75, 2.75], [0, 2], 'b')
# Línea recta D
ax.plot([3, 4], [1, 1], 'b')
ax.plot([3, 3], [0, 2], 'b')
ax.plot([3, 3.5], [0, 0], 'b')
ax.plot([3.5, 3.5], [0, 1], 'b')

# Dibujar el nombre "Dilan"
# Línea curva D
x = np.linspace(5, 6, 100)
y = 0.5 * np.sin(4 * np.pi * x) + 1.5
ax.plot(x, y, 'g')
ax.plot([5, 5], [0, 2], 'g')
ax.plot([5, 5.5], [0, 0], 'g')
ax.plot([5.5, 5.5], [0, 1], 'g')
# Línea recta I
ax.plot([6, 6], [0, 2], 'g')
# Línea recta L
ax.plot([6.25, 6.25], [0, 2], 'g')
ax.plot([6.25, 6.75], [2, 2], 'g')

# Dibujar el nombre "Adriana"
# Línea curva A
x = np.linspace(7, 8, 100)
y = 0.5 * np.sin(4 * np.pi * x) + 1
ax.plot(x, y, 'r')
ax.plot([7, 7], [0, 2], 'r')
ax.plot([7, 7.5], [2, 1], 'r')
ax.plot([7.5, 8], [1, 2], 'r')
# Línea recta D
ax.plot([8.25, 9], [1, 1], 'r')
ax.plot([8.25, 8.25], [0, 2], 'r')
ax.plot([8.25, 8.75], [0, 0], 'r')
ax.plot([8.75, 8.75], [0, 1], 'r')
# Línea recta R
ax.plot([9.25, 9.25], [0, 2], 'r')
ax.plot([9.25, 9.75], [2, 1], 'r')
ax.plot([9.25, 9.75], [1, 1], 'r')
ax.plot([9.75, 9.75], [1, 0], 'r')

# Configurar límites de los ejes
ax.set_xlim(0, 10)
ax.set_ylim(0, 2)

# Ocultar ejes
ax.axis('off')

# Mostrar el plot
plt.show()
