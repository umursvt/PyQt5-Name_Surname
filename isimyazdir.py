# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'isimyazdir.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from tkinter import Widget
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 289)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 40, 160, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbl_isim = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_isim.setObjectName("lbl_isim")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_isim)
        self.txt_isim = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_isim.setObjectName("txt_isim")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_isim)
        self.lbl_soyisim = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_soyisim.setObjectName("lbl_soyisim")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_soyisim)
        self.txt_soyisim = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_soyisim.setObjectName("txt_soyisim")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_soyisim)
        self.buton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.buton.setObjectName("buton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buton)
        self.lbl_sonuc = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_sonuc.setText("")
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lbl_sonuc)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "İlk Proje"))
        self.lbl_isim.setText(_translate("MainWindow", "isim:"))
        self.lbl_soyisim.setText(_translate("MainWindow", "soyisim:"))
        self.buton.setText(_translate("MainWindow", "Yazdır"))

