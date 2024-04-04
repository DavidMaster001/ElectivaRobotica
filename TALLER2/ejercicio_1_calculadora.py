import math

from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtGui import QPixmap

from ejercicio_1_calculadora_gui import Ui_MainWindow

class Calculadora(QMainWindow):
    """
    Ventana principal de la calculadora.
    """
    def __init__(self):
        """
        Constructor de la clase Calculadora.
        """
        super().__init__()

        self.setWindowTitle("Calculadora")
        self.setGeometry(0, 0, 800, 600)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_calcular_arit.clicked.connect(self.calcular_operacion_aritmetica)
        self.ui.btn_calcular_trig.clicked.connect(self.calcular_operacion_trigonometrica)

        imagen = QPixmap("logo.jpg")
        self.ui.lbl_imagen.setPixmap(imagen)

    def calcular_operacion_aritmetica(self):
        """
        Calcula la operación aritmética seleccionada.
        """
        num1 = float(self.ui.input_num1.text())
        num2 = float(self.ui.input_num2.text())
        resultado = None

        if self.ui.rb_suma.isChecked():
            resultado = num1 + num2
        elif self.ui.rb_resta.isChecked():
            resultado = num1 - num2
        elif self.ui.rb_multiplicacion.isChecked():
            resultado = num1 * num2
        elif self.ui.rb_division.isChecked():
            resultado = num1 / num2 if num2 != 0 else 'Error: División por cero'
        elif self.ui.rb_residuo.isChecked():
            resultado = num1 % num2 if num2 != 0 else 'Error: División por cero'

        self.ui.label_resultado_arit.setText(f"Resultado: {resultado}")

    def calcular_operacion_trigonometrica(self):
        """
        Calcula la operación trigonométrica seleccionada.
        """
        angulo = float(self.ui.input_angulo.text())
        resultado = None

        if self.ui.rb_seno.isChecked():
            resultado = math.sin(math.radians(angulo))
        elif self.ui.rb_coseno.isChecked():
            resultado = math.cos(math.radians(angulo))
        elif self.ui.rb_tangente.isChecked():
            resultado = math.tan(math.radians(angulo))
        elif self.ui.rb_cotangente.isChecked():
            resultado = 1 / math.tan(math.radians(angulo))
        elif self.ui.rb_secante.isChecked():
            resultado = 1 / math.cos(math.radians(angulo))
        elif self.ui.rb_cosecante.isChecked():
            resultado = 1 / math.sin(math.radians(angulo))

        self.ui.label_resultado_trig.setText(f"Resultado: {resultado}")


if __name__ == '__main__':
    app = QApplication([])
    ventana = Calculadora()
    ventana.show()
    app.exec_()
