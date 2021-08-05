# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Klasifikasi Kayu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import time
import os
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from program_utama.program_utama import meload_model, prediksi, prediksi_ann

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setFixedSize(888, 666)

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

        #self.prediksiGambar = QtWidgets.QPushButton(self.centralwidget)
        #self.prediksiGambar.setGeometry(QtCore.QRect(10, 490, 231, 41))
        #font = QtGui.QFont()
        #font.setPointSize(16)
        #self.prediksiGambar.setFont(font)
        #self.prediksiGambar.setObjectName("prediksiGambar")

        self.prediksiGambar2 = QtWidgets.QPushButton(self.centralwidget)
        self.prediksiGambar2.setGeometry(QtCore.QRect(10, 540, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.prediksiGambar2.setFont(font)
        self.prediksiGambar2.setObjectName("prediksiGambar2")

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
        self.bukaKamera.setObjectName("bukaKamera")

        self.tangkapGambar = QtWidgets.QPushButton(self.centralwidget)
        self.tangkapGambar.setGeometry(QtCore.QRect(40, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tangkapGambar.setFont(font)
        self.tangkapGambar.setObjectName("tangkapGambar")

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

        self.model, self.fc_model, self.clf = meload_model()

        self.bukaKamera.clicked.connect(self.membaca_frame)
        self.browseGambar.clicked.connect(self.tampil_gambar)
        #self.prediksiGambar.clicked.connect(self.memprediksi)
        self.tangkapGambar.clicked.connect(self.tangkap_gambar)
        self.prediksiGambar2.clicked.connect(self.memprediksi_ann)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Klasifikasi Kayu"))
        self.browseGambar.setText(_translate("MainWindow", "Browse Picture"))
        #self.prediksiGambar.setText(_translate("MainWindow", "Predict with CNN"))
        self.bukaKamera.setText(_translate("MainWindow", "Open Camera"))
        self.tangkapGambar.setText(_translate("MainWindow", "Capture Picture"))
        self.prediksiGambar2.setText(_translate("MainWindow", "Predict with ANN"))

    def tampil_gambar(self):

        self.listWidget.clear()
        self.probabilitasKayu.clear()

        #self.fc_model.load_weights("D:/Backup HDD Vajra/Backup File Laptop/Tugas Akhir/Program TA 2/Program Sendiri/Final/Klasifikasi Kayu/Final Data Scan/90_10/weights/fc_weights.hdf5")

        self.path_file, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Choosing Picture", "G:/Program TA/Aplikasi GUI", "Image Files (*.jpg *jpeg *.png)")
        
        if self.path_file:

            pixmap = QtGui.QPixmap(self.path_file)
            pixmap = pixmap.scaled(self.imageLabel.width(), self.imageLabel.height())
            self.imageLabel.setPixmap(pixmap)
            self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

    def memprediksi_ann(self):

        waktu_awal = time.time()

        nama_file, label, probabilitas = prediksi_ann(clf=self.clf, path_gambar=self.path_file)

        waktu_akhir = time.time()

        kalimat = nama_file + " adalah kelas " + label

        waktu_training = "Lama waktu prediksi : " + str(round(waktu_akhir-waktu_awal,2)) + " detik"

        # Probabilitas tiap kelas

        prob_kelas_I = "Kelas I\t= " + str(round(probabilitas[0][0]*100,2)) + "%"
        prob_kelas_II = "Kelas II\t= " + str(round(probabilitas[0][1]*100,2)) + "%"
        prob_kelas_III = "Kelas III\t= " + str(round(probabilitas[0][2]*100,2)) + "%"
        prob_kelas_IV = "Kelas IV\t= " + str(round(probabilitas[0][3]*100,2)) + "%"
        prob_kelas_V = "Kelas V\t= " + str(round(probabilitas[0][4]*100,2)) + "%"

        self.listWidget.addItem(kalimat)
        self.listWidget.addItem(waktu_training)

        self.probabilitasKayu.addItem(prob_kelas_I)
        self.probabilitasKayu.addItem(prob_kelas_II)
        self.probabilitasKayu.addItem(prob_kelas_III)
        self.probabilitasKayu.addItem(prob_kelas_IV)
        self.probabilitasKayu.addItem(prob_kelas_V)
    
    def memprediksi(self):

        waktu_awal = time.time()

        nama_file, label, probabilitas = prediksi(model=self.model, fc_model=self.fc_model, path_gambar=self.path_file)

        waktu_akhir = time.time()

        kalimat = nama_file + " adalah kelas " + label

        waktu_training = "Lama waktu prediksi : " + str(round(waktu_akhir-waktu_awal,2)) + " detik"

        # Probabilitas tiap kelas

        prob_kelas_I = "Kelas I\t= " + str(round(probabilitas[0][0]*100,2)) + "%"
        prob_kelas_II = "Kelas II\t= " + str(round(probabilitas[0][1]*100,2)) + "%"
        prob_kelas_III = "Kelas III\t= " + str(round(probabilitas[0][2]*100,2)) + "%"
        prob_kelas_IV = "Kelas IV\t= " + str(round(probabilitas[0][3]*100,2)) + "%"
        prob_kelas_V = "Kelas V\t= " + str(round(probabilitas[0][4]*100,2)) + "%"

        self.listWidget.addItem(kalimat)
        self.listWidget.addItem(waktu_training)

        self.probabilitasKayu.addItem(prob_kelas_I)
        self.probabilitasKayu.addItem(prob_kelas_II)
        self.probabilitasKayu.addItem(prob_kelas_III)
        self.probabilitasKayu.addItem(prob_kelas_IV)
        self.probabilitasKayu.addItem(prob_kelas_V)
    
    def membaca_frame(self):

        kamera = cv2.VideoCapture(0)

        while(True):

            _, frame = kamera.read()
        
            self.roi_frame = frame[0:480, 115:485]
        
            cv2.rectangle(frame, (115,0), (485,480), (0,0,0), 1)
        
            cv2.imshow("Frame Original",frame)

            if(cv2.waitKey(1) & 0xFF == ord('q')):
                break
    
        kamera.release()
        cv2.destroyAllWindows()
    
    
    def tangkap_gambar(self):

        self.listWidget.clear()
        self.probabilitasKayu.clear()

        #self.fc_model.load_weights("D:/Backup HDD Vajra/Backup File Laptop/Tugas Akhir/Program TA 2/Program Sendiri/Final/Klasifikasi Kayu/Final Data Foto/weights/fc_weights.hdf5")
        #self.fc_model.load_weights("G:/Github/Wood_Classification_Backpropagation_ANN/WooClass/Aplikasi GUI/model/weights.hdf5")

        cv2.imwrite("kayu_prediksi.jpg", self.roi_frame)

        self.path_file = os.path.join(os.getcwd(), "kayu_prediksi.jpg")

        if self.path_file:

            pixmap = QtGui.QPixmap(self.path_file)
            pixmap = pixmap.scaled(self.imageLabel.width(), self.imageLabel.height())
            self.imageLabel.setPixmap(pixmap)
            self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
