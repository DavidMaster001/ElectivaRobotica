#Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de
#la temperatura.

import math

# Coeficientes de la ecuación de Callendar-Van Dusen para una RTD de platino (PT100)
R0 = 100  
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12
TEMP = 25

R = R0 * (1 + A * TEMP + B * TEMP*2 + C * (TEMP - 100) * TEMP*3)  # Función para calcular la resistencia en función de la temperatura
print(f"\nLa resistencia a {TEMP} grados ° es de: {R:.2f} Ω \n")
