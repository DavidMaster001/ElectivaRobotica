
import matplotlib.pyplot as plt

D = [(0, 0), (0, 1), (1, 0.5), (0, 0)]
A = [(1, 0), (1.5, 1), (2, 0), (1.75, 0.5), (1.25, 0.5)]
V = [(2, 1), (2.5, 0), (3, 1)]
I = [(3.2, 1), (3.2, 0)]
D2 = [(3.5, 0), (3.5, 1), (4.5, 0.5), (3.5, 0)]

xD, yD = zip(*D)
xA, yA = zip(*A)
xV, yV = zip(*V)
xI, yI = zip(*I)
xD2, yD2 = zip(*D2)

plt.figure()

plt.plot(xD, yD, 'b-')
plt.plot(xA, yA, 'b-')
plt.plot(xV, yV, 'b-')
plt.plot(xI, yI, 'b-')
plt.plot(xD2, yD2, 'b-')

plt.xlim(-0.5, 5)
plt.ylim(-0.5, 1.5)

plt.show()