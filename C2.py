import numpy as np
import matplotlib.pyplot as plt

def analizar_y_graficar_funcion_transferencia():
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))
    coeficientes = [a, b, c]

    def segundo_orden(s):
        num = np.array([coeficientes[0]])  # Convertir a array de un solo elemento
        den = np.array(coeficientes[1:])   # Mantener como array si ya tiene más de un elemento
        return np.polyval(num, s) / np.polyval(den, s)

    def tipo_sistema():
        delta = coeficientes[1]**2 - 4*coeficientes[0]*coeficientes[2]
        if delta < 0:
            return 'Sistema subamortiguado'
        elif delta == 0:
            return 'Sistema críticamente amortiguado'
        else:
            return 'Sistema sobreamortiguado'

    def graficar_respuesta():
        t = np.linspace(0, 30, 1000)
        s = 1j * t  # 1j es para representar la unidad imaginaria
        y = segundo_orden(s)
        plt.plot(t, np.real(y), label='Parte real')
        plt.plot(t, np.imag(y), label='Parte imaginaria')
        plt.xlabel('Tiempo')
        plt.ylabel('Respuesta')
        plt.title('Respuesta del sistema')
        plt.legend()
        plt.grid()
        plt.show()

    print("El sistema es:", tipo_sistema())
    graficar_respuesta()

# Ejemplo de uso
analizar_y_graficar_funcion_transferencia()


#1,1,0.5 subamortiguado
#1,1,2 Criticamente amortiguado
#1,2,1 sobreamortiguado
