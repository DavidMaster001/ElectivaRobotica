#Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de
#la temperatura.

import math

# Coeficientes de la ecuación de Callendar-Van Dusen para una RTD de platino (PT100)
a = 3.9083e-3
b = -5.775e-7
R0 = 100  # Resistencia nominal a 0°C

# Función para calcular la resistencia en función de la temperatura
def cal_res(temperatura):
    R = R0 * (1 + a*temperatura + b*temperatura**2)
    return R

# Ejemplo de uso
temperatura = 100  # Temperatura en grados Celsius
resistencia = cal_res(temperatura)
print(f"Para una temperatura de {temperatura}°C, la resistencia es de {resistencia} ohmios")
