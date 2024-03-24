import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear un QLabel
        self.label = QLabel(self)

        # Cargar la imagen desde el archivo .qrc
        pixmap = QPixmap("descargar.png")  # Reemplaza 'mi_imagen.png' por el nombre de tu imagen
        self.label.setPixmap(pixmap)

        # Ajustar el tamaño de la ventana al tamaño de la imagen
        self.resize(pixmap.width(), pixmap.height())

        # Establecer el título de la ventana
        self.setWindowTitle("Imagen en QLabel")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
