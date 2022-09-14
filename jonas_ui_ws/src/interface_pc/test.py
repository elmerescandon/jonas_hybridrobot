#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
from std_msgs.msg import String
# from PyQt5 import QtGui

import sys

from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI_design import *


class UI_MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(UI_MainWindow,self).__init__(*args,**kwargs)
        setupUi(self)
        self.pub = rospy.Publisher('pyqt_topic',String,queue_size = 10)  
        rospy.init_node('pyqt_gui')
        self.slider.valueChanged.connect(self.changeValue)
        self.current_value = 0


    def publish_topic(self):
        self.pub.publish(str(self.current_value))

    def changeValue(self,value):
        self.my_label.setText("num: " + str(value))
        self.current_value = value
        self.publish_topic()
        


    # def retranslateUi(self, QMainWindow):


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ui = UI_MainWindow()
    ui.show()
    sys.exit(app.exec_())



# class PyGui(QMainWindow):
#     def __init__(self, *args, **kwargs):

#         super(PyGui,self).__init__(*args,**kwargs)
#         self.setFixedWidth(800)
#         self.setFixedHeight(600)

#         # Inicializar el objeto principal
#         self.centralwidget = QWidget()
#         self.centralwidget.setObjectName("centralwidget")

#         self.pub = rospy.Publisher('pyqt_topic',String,queue_size = 10)   

#         # Iniciar ROS
#         rospy.init_node('pyqt_gui')
#         self.current_value = 0

#         my_layout = QHBoxLayout(self.centralwidget)

#         my_btn = QPushButton(self.centralwidget)
#         my_btn.setText("Publisher") 
#         my_btn.setFixedWidth(130)
#         my_btn.clicked.connect(self.publish_topic)


#         my_layout.addWidget(my_btn)
#         my_layout.addSpacing(50)

#         self.my_label = QLabel(self.centralwidget)
#         self.my_label.setFixedWidth(140)
#         self.my_label.setText("num: " + str(0))
#         self.my_label.setEnabled(False)

#         my_layout.addWidget(self.my_label)

#         my_slider = QSlider(self.centralwidget)
#         my_slider.setMinimum(0)
#         my_slider.setMaximum(99)
#         my_slider.setOrientation(Qt.Horizontal)
#         my_slider.valueChanged.connect(self.changeValue)

#         my_vlay = QVBoxLayout(self.centralwidget)
#         my_vlay.addWidget(my_slider)
        
#         layout = QVBoxLayout(self.centralwidget)
#         layout.addLayout(my_layout)
#         layout.addLayout(my_vlay)
#         self.setLayout(layout)

#     def publish_topic(self):
#         self.pub.public(str(self.current_value))

#     def changeValue(self,value):
#         self.my_label.setText("num: " + str(value))
#         self.current_value = value

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyle('Fusion')
    
#     ui = PyGui()
#     ui.show()

#     sys.exit(app.exec_())



