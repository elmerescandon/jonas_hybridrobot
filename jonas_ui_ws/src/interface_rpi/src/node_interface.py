#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

path_of_image = ['faces/smile_1.png','faces/smile_2.png','faces/smile_3.png','faces/smile_4.png']

class App(QtWidgets.QWidget):
    def __init__(self):
        super(App,self).__init__()
        self.title = 'My Screen'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.image_count = 0
        self.reverse = False
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label = QtWidgets.QLabel(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_image)
        timer.start(200)
        self.showFullScreen()
        self.update_image()
        

    def update_image(self):
        pixmap = QtGui.QPixmap(path_of_image[self.image_count])
        if not pixmap.isNull():
            self.label.setPixmap(pixmap)
            self.label.adjustSize()
            self.resize(pixmap.size())

            if self.image_count >= 3 and self.reverse == False:
                self.reverse = True
            elif self.image_count == 0 and self.reverse == True:
                self.reverse = False

            if (self.reverse):
                self.image_count -= 1
            else:
                self.image_count += 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())