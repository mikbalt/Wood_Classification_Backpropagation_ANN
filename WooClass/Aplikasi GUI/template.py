# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Klasifikasi Kayu.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browseGambar = QtWidgets.QPushButton(self.centralwidget)
        self.browseGambar.setGeometry(QtCore.QRect(40, 340, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.browseGambar.setFont(font)
        self.browseGambar.setObjectName("browseGambar")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(260, 490, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(250, 10, 631, 471))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.prediksiGambar = QtWidgets.QPushButton(self.centralwidget)
        self.prediksiGambar.setGeometry(QtCore.QRect(10, 490, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.prediksiGambar.setFont(font)
        self.prediksiGambar.setObjectName("prediksiGambar")
        self.probabilitasKayu = QtWidgets.QListWidget(self.centralwidget)
        self.probabilitasKayu.setGeometry(QtCore.QRect(590, 490, 281, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.probabilitasKayu.setFont(font)
        self.probabilitasKayu.setObjectName("probabilitasKayu")
        self.bukaKamera = QtWidgets.QPushButton(self.centralwidget)
        self.bukaKamera.setGeometry(QtCore.QRect(40, 110, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bukaKamera.setFont(font)
        self.bukaKamera.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bukaKamera.setObjectName("bukaKamera")
        self.tangkapGambar = QtWidgets.QPushButton(self.centralwidget)
        self.tangkapGambar.setGeometry(QtCore.QRect(40, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tangkapGambar.setFont(font)
        self.tangkapGambar.setObjectName("tangkapGambar")
        self.prediksiGambar2 = QtWidgets.QPushButton(self.centralwidget)
        self.prediksiGambar2.setGeometry(QtCore.QRect(10, 540, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.prediksiGambar2.setFont(font)
        self.prediksiGambar2.setObjectName("prediksiGambar2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Klasifikasi Kayu"))
        self.browseGambar.setText(_translate("MainWindow", "Browse Gambar"))
        self.prediksiGambar.setText(_translate("MainWindow", "Predict with CNN"))
        self.bukaKamera.setText(_translate("MainWindow", "Buka Kamera"))
        self.tangkapGambar.setText(_translate("MainWindow", "Tangkap Gambar"))
        self.prediksiGambar2.setText(_translate("MainWindow", "Predict with ANN"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
