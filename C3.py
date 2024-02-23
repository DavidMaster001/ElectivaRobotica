import numpy as np
import matplotlib.pyplot as plt

def carga_descarga_RC(V, C, R, tiempo):
    # Constante de tiempo (tau)
    tau = R * C
    
    # Carga
    carga = V * (1 - np.exp(-tiempo / tau))
    
    # Descarga
    descarga = V * np.exp(-tiempo / tau)
    
    return carga, descarga

def graficar_carga_descarga(tiempo, carga, descarga):
    plt.plot(tiempo, carga, label='Carga')
    plt.plot(tiempo, descarga, label='Descarga')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (V)')
    plt.title('Carga y Descarga de un Circuito RC')
    plt.legend()
    plt.grid()
    plt.show()

# Entrada de datos por el usuario
V = float(input("Ingrese el valor de voltaje (V): "))
C = float(input("Ingrese el valor de capacitancia (µF): "))
R = float(input("Ingrese el valor de resistencia (Ω): "))

C = C*1e-6
tiempo = np.linspace(0, 5*R*C, 1000)  # Tiempo de 0 a 5*tau

# Cálculo de carga y descarga
carga, descarga = carga_descarga_RC(V, C, R, tiempo)

# Gráfico
graficar_carga_descarga(tiempo, carga, descarga)
