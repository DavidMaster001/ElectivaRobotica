
import matplotlib.pyplot as plt

D = [(0, 0), (0, 1), (1, 0.5), (0, 0)]
I = [(1.2, 0), (1.2, 1)]
L = [(2.2, 0), (1.5, 0), (1.5, 1)]
A = [(2.5, 0), (3, 1), (3.5, 0), (3.25, 0.5), (2.75, 0.5)]
N = [(3.7, 0), (3.7, 1), (4.5, 0), (4.5, 1)]

xD, yD = zip(*D)
xI, yI = zip(*I)
xL, yL = zip(*L)
xA, yA = zip(*A)
xN, yN = zip(*N)

plt.plot(xD, yD, 'b-')
plt.plot(xI, yI, 'b-')
plt.plot(xL, yL, 'b-')
plt.plot(xA, yA, 'b-')
plt.plot(xN, yN, 'b-')

plt.xlim(-0.5, 5)
plt.ylim(-0.5, 1.5)

plt.show()
