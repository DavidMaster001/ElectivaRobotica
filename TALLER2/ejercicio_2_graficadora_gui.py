# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejercicio_2_graficadora_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 413)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lbl_funcion = QtWidgets.QLabel(self.centralwidget)
        self.lbl_funcion.setObjectName("lbl_funcion")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_funcion)
        self.lbl_valor_minimo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_valor_minimo.setObjectName("lbl_valor_minimo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_valor_minimo)
        self.input_minimo = QtWidgets.QSpinBox(self.centralwidget)
        self.input_minimo.setMinimum(-100)
        self.input_minimo.setMaximum(100)
        self.input_minimo.setObjectName("input_minimo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_minimo)
        self.lbl_valor_maximo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_valor_maximo.setObjectName("lbl_valor_maximo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_valor_maximo)
        self.input_maximo = QtWidgets.QSpinBox(self.centralwidget)
        self.input_maximo.setMinimum(-100)
        self.input_maximo.setMaximum(100)
        self.input_maximo.setObjectName("input_maximo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_maximo)
        self.btn_graficar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_graficar.setObjectName("btn_graficar")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btn_graficar)
        self.btn_seleccionar_funcion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_seleccionar_funcion.setObjectName("btn_seleccionar_funcion")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btn_seleccionar_funcion)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lbl_imagen = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagen.setText("")
        self.lbl_imagen.setObjectName("lbl_imagen")
        self.gridLayout.addWidget(self.lbl_imagen, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.mbr_principal = QtWidgets.QMenuBar(MainWindow)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 671, 21))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_funcion.setText(_translate("MainWindow", "Funcion:"))
        self.lbl_valor_minimo.setText(_translate("MainWindow", "Valor mínimo:"))
        self.lbl_valor_maximo.setText(_translate("MainWindow", "Valor máximo:"))
        self.btn_graficar.setText(_translate("MainWindow", "Graficar"))
        self.btn_seleccionar_funcion.setText(_translate("MainWindow", "Seleccione función..."))
        self.label.setText(_translate("MainWindow", "Adriana Bolivar Bolivar\n"
"Jonathan David Pinto Bucuru\n"
"Dyllam Arévalo Velásquez"))
        self.mnu_archivo.setTitle(_translate("MainWindow", "Archivo"))
        self.mni_salir.setText(_translate("MainWindow", "Salir"))
