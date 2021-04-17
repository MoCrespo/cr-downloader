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
        self.handel_buttons()

    def handel_UI(self):
        self.setWindowTitle("Cr Downloader")
        self.setFixedSize(540,242)

    def handel_buttons(self):
        self.pushButton.clicked.connect(self.download)
        self.pushButton_2.clicked.connect(self.handel_browse) 

    def handel_browse(self):
        save_place = QFileDialog.getSaveFileName(self, caption="Save As", directory=".", filter="All Files (*.*)")
        text = str(save_place)
        name = (text[2:].split(',')[0].replace("'", ''))
        self.lineEdit_2.setText(name)

    def handel_progress(self, blocknum, blocksize, totalsize):
        read = blocknum * blocksize

        if totalsize > 0:
            percent = read * 100 / totalsize
            self.progressBar.setValue(percent)
            QApplication.processEvents() # Not Responding 

    def download(self):
        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        try:

            urllib.request.urlretrieve(url, save_location, self.handel_progress)
        except Exception:
            QMessageBox.warning(self, "Download Error", "The download faild")
            return
        QMessageBox.information(self, "Download Completed", "The download finished")
        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')

def main():
    app = QApplication(sys.argv)
    window = main_app()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()