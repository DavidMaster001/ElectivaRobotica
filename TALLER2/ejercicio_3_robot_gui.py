# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejercicio_3_robot_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.verticalLayout.addWidget(self.label_info)
        self.view = QtWidgets.QGraphicsView(self.centralwidget)
        self.view.setObjectName("view")
        self.verticalLayout.addWidget(self.view)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lbl_imagen = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagen.setText("")
        self.lbl_imagen.setObjectName("lbl_imagen")
        self.gridLayout.addWidget(self.lbl_imagen, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.mbr_principal = QtWidgets.QMenuBar(MainWindow)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 564, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        self.mnu_archivo = QtWidgets.QMenu(self.mbr_principal)
        self.mnu_archivo.setObjectName("mnu_archivo")
        MainWindow.setMenuBar(self.mbr_principal)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mni_salir = QtWidgets.QAction(MainWindow)
        self.mni_salir.setObjectName("mni_salir")
        self.mnu_archivo.addAction(self.mni_salir)
        self.mbr_principal.addAction(self.mnu_archivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robots"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Cartesiano"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Esférico"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Cilíndrico"))
        self.label.setText(_translate("MainWindow", "Adriana Bolivar Bolivar\n"
"Jonathan David Pinto Bucuru\n"
"Dyllam Arévalo Velásquez"))
        self.mnu_archivo.setTitle(_translate("MainWindow", "Archivo"))
        self.mni_salir.setText(_translate("MainWindow", "Salir"))
