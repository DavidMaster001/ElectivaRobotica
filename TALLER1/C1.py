import numpy as np
import matplotlib.pyplot as plt

# Función para convertir la resistencia a temperatura para PT100
def pt100_resistance_to_temperature(resistance):
    # Coeficientes de la ecuación de Callendar-Van Dusen para PT100
    a = 3.9083e-3
    b = -5.775e-7
    R0 = 100.0  # Resistencia a 0°C
    
    # Cálculo de la temperatura
    temperature = (-R0 * a + np.sqrt(R0**2 * a**2 - 4 * R0 * b * (R0 - resistance))) / (2 * R0 * b)
    return temperature

# Rango de resistencias
resistencias = np.linspace(10, 400, 1000) #se utiliza para generar un arreglo de números espaciados de manera uniforme en un intervalo especificado

# Convertir resistencias a temperatura
temperatures = pt100_resistance_to_temperature(resistencias)

# Graficar
plt.plot(temperatures, resistencias) #grafique temp(x) y resistecia(Y)
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohm)')
plt.title('Sensor PT100')
plt.xlim(-200, 200) #Limitar la grafica 
plt.grid(True)#la cuadricula
plt.show()#lo muestre en la pantalla :D