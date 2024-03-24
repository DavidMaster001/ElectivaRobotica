
import RPi.GPIO as GPIO
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# Cargar la interfaz gráfica diseñada en Qt Designer
Ui_MainWindow, QtBaseClass = uic.loadUiType("taller2.ui")

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)

        # Configurar pines GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)

        # Conectar eventos de los objetos GUI a funciones
        self.slider.valueChanged.connect(self.slider_changed)
        self.servo_edit.textChanged.connect(self.servo_edit_changed)

    def slider_changed(self, value):
        # Obtener el ángulo del slider
        angle = value

        # Obtener el número de servo desde el campo de edición de texto
        servo_num = int(self.servo_edit.text())

        # Mover el servo correspondiente al ángulo seleccionado
        if servo_num == 1:
            GPIO.output(17, GPIO.HIGH)
            # Lógica para mover el servo 1 al ángulo
            GPIO.output(17, GPIO.LOW)
        elif servo_num == 2:
            GPIO.output(18, GPIO.HIGH)
            # Lógica para mover el servo 2 al ángulo
            GPIO.output(18, GPIO.LOW)

        # Actualizar el campo de texto estático con el ángulo actual
        self.angle_label.setText(f"Ángulo actual: {angle}°")

    def servo_edit_changed(self, text):
        # Manejar cambios en el campo de edición de texto
        pass

if __name__ == "__main__":
    GPIO.setwarnings(False)
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
