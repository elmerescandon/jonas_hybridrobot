#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy

from std_msgs.msg import Int8
from PyQt5 import QtCore, QtGui, QtWidgets

main_path = '/home/raul/jonas_hybridrobot/jonas_ui_ws/src/interface_rpi/src/faces'

path_of_image = [ main_path + '/smile_1.png', main_path + '/smile_2.png', main_path + '/smile_3.png', main_path + '/smile_4.png']


def callback_face(data,self):
    print(data.data)
    self.image_count = data.data


class App(QtWidgets.QWidget):
    def __init__(self):
        super(App,self).__init__()
        # Initialize variables
        self.title = 'My Screen'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.image_count = 0
        self.reverse = False

        # ROS Variables 
        rospy.init_node('node_interface')
        self.pub_face = rospy.Subscriber('face_coms_topic',Int8,callback_face,(self))


        # Construct GUI
        self.initUI()
        
        

    def initUI(self):
        print(path_of_image)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label = QtWidgets.QLabel(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_image)
        timer.start(200)
        # self.showFullScreen()
        self.update_image()
        

    def update_image(self):
        pixmap = QtGui.QPixmap(path_of_image[self.image_count])
        if not pixmap.isNull():
            self.label.setPixmap(pixmap)
            self.label.adjustSize()
            self.resize(pixmap.size())

            # if self.image_count >= 3 and self.reverse == False:
            #     self.reverse = True
            # elif self.image_count == 0 and self.reverse == True:
            #     self.reverse = False

            # if (self.reverse):
            #     self.image_count -= 1
            # else:
            #     self.image_count += 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())