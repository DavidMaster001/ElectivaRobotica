import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenu, QAction, QLabel, QComboBox, QVBoxLayout, QWidget, QGraphicsView, QGraphicsScene)
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.image as mpimg

from ejercicio_3_robot_gui import Ui_MainWindow

class MplCanvas(FigureCanvasQTAgg):
    """
    Clase para mostrar gráficos de matplotlib en una ventana de PyQt5.
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        Constructor de la clase MplCanvas.

        :param parent: Widget padre.
        :param width: Ancho del gráfico.
        :param height: Alto del gráfico.
        :param dpi: Resolución del gráfico.
        """
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selector de Tipos de Robot")
        self.setGeometry(100, 100, 800, 600)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.currentIndexChanged.connect(self.update_info)

        self.scene = QGraphicsScene()
        self.ui.view.setScene(self.scene)

        imagen = QPixmap("logo.jpg")
        self.ui.lbl_imagen.setPixmap(imagen)

    def update_info(self, index):
        robot_info = [
            {"name": "Cartesiano", "joints": "3 articulaciones P-P-P", "image": "robot_cartesiano.jpg"},
            {"name": "Esferico", "joints": "3 articulaciones R-P-P", "image": "robot_esferico.jpg"},
            {"name": "Cilindrico", "joints": "3 articulaciones R-P-P", "image": "robot_cilindrico.jpg"},
        ]

        info = robot_info[index]
        self.ui.label_info.setText(f"{info['name']}:\n{info['joints']}")

        imagen = mpimg.imread(info['image'])

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        self.canvas.axes.imshow(imagen)
        self.canvas.axes.axis('off')

        self.scene.addWidget(self.canvas)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
