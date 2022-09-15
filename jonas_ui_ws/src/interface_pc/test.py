#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16MultiArray
# from PyQt5 import QtGui

import sys

from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI_design import *


class UI_MainWindow(QMainWindow):
    def __init__(sel,*args,**kwargs):
        super(UI_MaifnWindow,self).__init__(*args,**kwargs)
        setupUi(self)

        # Initialize nodes
        rospy.init_node('pyqt_gui')

        # Create topics
        self.pub_mov = rospy.Publisher('mov_coms_topic',Int16MultiArray,queue_size = 10)  
        self.pub_face = rospy.Publisher('face_coms_topic',String,queue_size = 10)
        self.pub_servos_commands = rospy.Publisher('servos_coms_topic',String,queue_size = 10)


        # Additional Widgets
        self.slider.valueChanged.connect(self.changeValue)

        self.timer_mov = QTimer()   
        self.timer_mov.timeout.connect(self.button_timeout)

        self.direction = ''
        self.current_value = 0
 
        # Message to send - Multiarray
        self.mov_msg = Int16MultiArray()

        self.mov_dic = {'UP': 1, 'DOWN': 2, 'LEFT':3, 'RIGHT':4}

    def set_face(self,expression):
        self.pub_face.publish(expression)

    def set_servos(self,gesture):
        self.pub_servos_commands.publish(gesture)

    def button_pressed(self, direction):
        self.direction = direction
        self.timer_mov.start(100)

    def button_released(self):
        self.timer_mov.stop()
    
    def button_timeout(self):
        self.mov_msg.data = [self.mov_dic[self.direction],self.current_value]
        print(self.direction)
        print(self.current_value)
        self.pub_mov.publish(self.mov_msg)

    def changeValue(self,value):
        self.my_label.setText("num: " + str(value))
        self.current_value = value
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ui = UI_MainWindow()
    ui.show()
    sys.exit(app.exec_())


