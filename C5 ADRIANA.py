import matplotlib.pyplot as plt

# Coordenadas de las letras
A = [(0, 0), (0.5, 1), (1, 0), (0.8, 0.4), (0.2, 0.4)]
D = [(1.5, 0), (1.5, 1), (2, 0.5), (1.5, 0)]
R = [(2.5, 0), (2.5, 1), (3.2, 0.7), (2.5, 0.5), (3.2, 0)]
I = [(3.6, 0), (3.6, 1)]
A2 = [(4, 0), (4.5, 1), (5, 0), (4.8, 0.4), (4.2, 0.4)]
N = [(5.5, 0), (5.5, 1), (6, 0), (6, 1)]
A3 = [(6.5, 0), (7, 1), (7.5, 0), (7.3, 0.4), (6.7, 0.4)]

# Desempaquetar las coordenadas para cada letra
xA, yA = zip(*A)
xD, yD = zip(*D)
xR, yR = zip(*R)
xI, yI = zip(*I)
xA2, yA2 = zip(*A2)
xN, yN = zip(*N)
xA3, yA3 = zip(*A3)

# Trazar las líneas para cada letra
plt.plot(xA, yA, 'b-')
plt.plot(xD, yD, 'b-')
plt.plot(xR, yR, 'b-')
plt.plot(xI, yI, 'b-')
plt.plot(xA2, yA2, 'b-')
plt.plot(xN, yN, 'b-')
plt.plot(xA3, yA3, 'b-')

# Establecer límites del eje x e y
plt.xlim(-0.5, 8)
plt.ylim(-0.5, 1.5)

# Mostrar el gráfico
plt.show()
