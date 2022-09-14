# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def setupUi(self):

    self.setStyleSheet("background-color: white;")
    self.setFixedWidth(800)
    self.setFixedHeight(600)
    # MainWindow.setObjectName("MainWindow")
    # MainWindow.resize(803, 525)
    # MainWindow.setStyleSheet("")
    self.centralwidget = QWidget()
    self.centralwidget.setObjectName("centralwidget")
    self.centralwidget.setWindowModality(Qt.NonModal)
    # self.centralwidget.resize(1153, 587)
    palette = QPalette()
    self.centralwidget.setPalette(palette)
    self.centralwidget.setStyleSheet("")

    self.textBrowser = QTextBrowser(self.centralwidget)
    self.textBrowser.setGeometry(QRect(290, 20, 271, 41))
    self.textBrowser.setStyleSheet("background-color:transparent;")
    self.textBrowser.setObjectName("textBrowser")
    self.textBrowser.setText("Robot Jonas")

    self.D_button = QPushButton(self.centralwidget)
    self.D_button.setGeometry(QRect(370, 330, 50, 50))
    self.D_button.setObjectName("D_button")
    self.D_button.pressed.connect(lambda: self.button_pressed('DOWN'))
    self.D_button.released.connect(self.button_released)

    self.L_button = QPushButton(self.centralwidget)
    self.L_button.setGeometry(QRect(530, 240, 50, 50))
    self.L_button.setObjectName("L_button")
    self.L_button.pressed.connect(lambda: self.button_pressed('LEFT'))
    self.L_button.released.connect(self.button_released)

    self.U_button = QPushButton(self.centralwidget)
    self.U_button.setGeometry(QRect(380, 160, 50, 50))
    self.U_button.setObjectName("U_button")
    self.U_button.pressed.connect(lambda: self.button_pressed('UP'))
    self.U_button.released.connect(self.button_released)

    self.R_button = QPushButton(self.centralwidget)
    self.R_button.setGeometry(QRect(230, 250, 50, 50))
    self.R_button.setObjectName("R_button")
    self.R_button.pressed.connect(lambda: self.button_pressed('RIGHT'))
    self.R_button.released.connect(self.button_released)

    self.UR_button = QPushButton(self.centralwidget)
    self.UR_button.setGeometry(QRect(450, 200, 50, 50))
    self.UR_button.setObjectName("UR_button")


    self.DR_button = QPushButton(self.centralwidget)
    self.DR_button.setGeometry(QRect(450, 290, 50, 50))
    self.DR_button.setObjectName("DR_button")


    self.DL_button = QPushButton(self.centralwidget)
    self.DL_button.setGeometry(QRect(300, 290, 50, 50))
    self.DL_button.setObjectName("DL_button")


    self.UL_button = QPushButton(self.centralwidget)
    self.UL_button.setGeometry(QRect(300, 200, 50, 50))
    self.UL_button.setObjectName("UL_button")


    # Diseño de todos los gestos posibles

    self.face1_button = QPushButton(self.centralwidget)
    self.face1_button.setGeometry(QRect(660, 90, 80, 61))
    self.face1_button.setObjectName("face1_button")
    self.face1_button.clicked.connect(lambda: self.set_face('CARA 1'))
    self.face1_button.clicked.connect(lambda: self.set_servos('GESTO 1'))

    self.face2_button = QPushButton(self.centralwidget)
    self.face2_button.setGeometry(QRect(660, 170, 80, 61))
    self.face2_button.setObjectName("face2_button")
    self.face2_button.clicked.connect(lambda: self.set_face('CARA 2'))
    self.face2_button.clicked.connect(lambda: self.set_servos('GESTO 2'))

    self.face3_button = QPushButton(self.centralwidget)
    self.face3_button.setGeometry(QRect(660, 250, 80, 61))
    self.face3_button.setObjectName("face3_button")
    self.face3_button.clicked.connect(lambda: self.set_face('CARA 3'))
    self.face3_button.clicked.connect(lambda: self.set_servos('GESTO 3'))

    self.face4_button = QPushButton(self.centralwidget)
    self.face4_button.setGeometry(QRect(660, 330, 80, 61))
    self.face4_button.setObjectName("face4_button")
    self.face4_button.clicked.connect(lambda: self.set_face('CARA 4'))
    self.face4_button.clicked.connect(lambda: self.set_servos('GESTO 4'))

    self.face5_button = QPushButton(self.centralwidget)
    self.face5_button.setGeometry(QRect(660, 400, 80, 61))
    self.face5_button.setObjectName("face5_button")
    self.face5_button.clicked.connect(lambda: self.set_face('CARA 5'))
    self.face5_button.clicked.connect(lambda: self.set_servos('GESTO 5'))
    
    self.START_button =QPushButton(self.centralwidget)
    self.START_button.setGeometry(QRect(50, 150, 111, 51))
    self.START_button.setObjectName("START_button")


    self.STOP_button = QPushButton(self.centralwidget)
    self.STOP_button.setGeometry(QRect(50, 210, 111, 51))
    self.STOP_button.setObjectName("STOP_button")


    self.slider = QSlider(self.centralwidget)
    self.slider.setMinimum(0)
    self.slider.setMaximum(99)
    self.slider.setOrientation(Qt.Horizontal)

    self.my_label = QLabel(self.centralwidget)
    self.my_label.setFixedWidth(140)
    self.my_label.setGeometry(200, 100, 300, 80)
    self.my_label.setText("num: " + str(0))
    self.my_label.setEnabled(False)

    _translate = QCoreApplication.translate
    self.centralwidget.setWindowTitle(_translate("MainWindow", "MainWindow"))
    
    self.UR_button.setText(_translate("MainWindow", "UR"))
    self.DR_button.setText(_translate("MainWindow", "DR"))
    self.DL_button.setText(_translate("MainWindow", "DL"))
    self.UL_button.setText(_translate("MainWindow", "UL"))
    self.face2_button.setText(_translate("MainWindow", "Secuencia 2"))
    self.face1_button.setText(_translate("MainWindow", "Secuencia 1"))
    self.face3_button.setText(_translate("MainWindow", "Secuencia 3"))
    self.face4_button.setText(_translate("MainWindow", "Secuencia 4"))
    self.face5_button.setText(_translate("MainWindow", "Secuencia 5"))
    self.D_button.setText(_translate("MainWindow", "DOWN"))
    self.L_button.setText(_translate("MainWindow", "LEFT"))
    self.U_button.setText(_translate("MainWindow", "UP"))
    self.R_button.setText(_translate("MainWindow", "RIGHT"))
    self.START_button.setText(_translate("MainWindow", "START"))
    self.STOP_button.setText(_translate("MainWindow", "STOP"))

    QMetaObject.connectSlotsByName(self.centralwidget)
    self.setCentralWidget(self.centralwidget)