from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType


import os 
from os import path
import sys
import urllib.request

FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"main.ui"))


class main_app(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(main_app,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_UI()

    def handel_UI(self):
        self.setWindowTitle("Cr Downloader")
        self.setFixedSize(540,242)

    def handel_buttons(self):
        pass 

    def handel_browse(self):
        pass 

    def handel_progress(self):
        pass

    def download(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = main_app()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()