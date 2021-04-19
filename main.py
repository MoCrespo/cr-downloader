from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType


import os 
from os import path
import sys
import pafy
from pytube import Playlist
import humanize
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
        self.setFixedSize(551,242)

    def handel_buttons(self):
        self.pushButton.clicked.connect(self.download)
        self.pushButton_2.clicked.connect(self.handel_browse)
        self.pushButton_4.clicked.connect(self.download_youtube_video)
        self.pushButton_5.clicked.connect(self.get_youtube_video)
        self.pushButton_3.clicked.connect(self.save_browse)
        self.pushButton_9.clicked.connect(self.download_playlist) 
        self.pushButton_10.clicked.connect(self.save_browse)


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

    def save_browse(self):
        save = QFileDialog.getExistingDirectory(self, "Select download directory")
        self.lineEdit_3.setText(save)
        self.lineEdit_10.setText(save)

    def get_youtube_video(self):
        video_link = self.lineEdit_4.text()
        v = pafy.new(video_link)
        st = v.allstreams
        for s in st:
            size = humanize.naturalsize(s.get_filesize())
            data = '{} {} {} {}'.format(s.mediatype, s.extension, s.quality, size)
            self.comboBox.addItem(data)

    def download_youtube_video(self):
        video_link = self.lineEdit_4.text()
        save_location = self.lineEdit_3.text()
        v = pafy.new(video_link)
        st = v.allstreams
        quality = self.comboBox.currentIndex()
        down = st[quality].download(filepath=save_location)
        QMessageBox.information(self, "Download Completed", "The download finished")

    def download_playlist(self):
        playlist_url = self.lineEdit_9.text()
        save_location = self.lineEdit_10.text()
        playlist = Playlist(playlist_url)

        os.chdir(save_location)
        if os.path.exists(str(playlist.title)):
            os.chdir(str(playlist.title))
        else:
            os.mkdir(str(playlist.title))
            os.chdir(str(playlist.title))

        for video in playlist.videos:
            video.streams.first().download()



def main():
    app = QApplication(sys.argv)
    window = main_app()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()