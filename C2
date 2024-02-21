import numpy as np
import matplotlib.pyplot as plt

def analizar_y_graficar_funcion_transferencia(coeficientes):
    def segundo_orden(s):
        num = coeficientes[0]
        den = coeficientes[1:]
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
        s = 1j * t
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
coeficientes = [1, 1, 1]  # Ejemplo de coeficientes
analizar_y_graficar_funcion_transferencia(coeficientes)
