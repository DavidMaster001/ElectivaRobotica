import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QPushButton,
                             QLineEdit, QWidget, QLabel, QMenu)
from PyQt5.QtGui import QPixmap

from ejercicio_2_graficadora_gui import Ui_MainWindow

class VentanaPrincipal(QMainWindow):
    """
    Ventana principal de la aplicación.
    """
    def __init__(self):
        """
        Constructor de la clase VentanaPrincipal.
        """
        super().__init__()

        self.setWindowTitle("Graficador de Funciones Trigonométricas")
        self.setGeometry(100, 100, 600, 400)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.menu_funciones = QMenu(self)
        self.menu_funciones.addAction('Seno', lambda: self.seleccionar_funcion('seno'))
        self.menu_funciones.addAction('Coseno', lambda: self.seleccionar_funcion('coseno'))
        self.menu_funciones.addAction('Tangente', lambda: self.seleccionar_funcion('tangente'))
        self.menu_funciones.addAction('Cotangente', lambda: self.seleccionar_funcion('cotangente'))
        self.menu_funciones.addAction('Secante', lambda: self.seleccionar_funcion('secante'))
        self.menu_funciones.addAction('Cosecante', lambda: self.seleccionar_funcion('cosecante'))

        self.ui.btn_seleccionar_funcion.setMenu(self.menu_funciones)

        self.ui.btn_graficar.clicked.connect(self.graficar)

        self.funcion_actual = None
        
        imagen = QPixmap("logo.jpg")
        self.ui.lbl_imagen.setPixmap(imagen)


    def seleccionar_funcion(self, funcion):
        """
        Selecciona la función trigonométrica a graficar.
        """
        self.funcion_actual = funcion


    def graficar(self):
        """
        Grafica la función trigonométrica seleccionada.
        """

        if self.funcion_actual is None:
            return
        
        self.rango_minimo = float(self.ui.input_minimo.text())
        self.rango_maximo = float(self.ui.input_maximo.text())

        x = np.linspace(self.rango_minimo, self.rango_maximo, 400)

        if self.funcion_actual == 'seno':
            y = np.sin(x)
        elif self.funcion_actual == 'coseno':
            y = np.cos(x)
        elif self.funcion_actual == 'tangente':
            y = np.tan(x)
        elif self.funcion_actual == 'cotangente':
            y = 1 / np.tan(x)
        elif self.funcion_actual == 'secante':
            y = 1 / np.cos(x)
        elif self.funcion_actual == 'cosecante':
            y = 1 / np.sin(x)
        
        plt.figure()
        plt.plot(x, y)
        plt.title(f'Función {self.funcion_actual.capitalize()}')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid()
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
