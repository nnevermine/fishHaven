from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize

class FishFrame(QGroupBox):
    
    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)
        self.addInfo(info)

    def addInfo(self, info):
        low_rez = QSize(100, 100)
        pixmap = QPixmap('./assets/images/sprites/1.png')
        label = QLabel(self)
        if info[3] == "sick salmon":
            pixmap = QPixmap('./assets/images/sprites/1.png')
        elif info[3] == "peem":
            pixmap = QPixmap('./assets/images/sprites/peem.png')
        elif info[3] == "dang":
            pixmap = QPixmap('./assets/images/sprites/dang.png')
        elif info[3] == "pla":
            #have to change this to a different image
            pixmap = QPixmap('./assets/images/sprites/pla.png')
        pixmap = pixmap.scaled(low_rez)
        label.setPixmap(pixmap)
        self.addLabel(label)
        for i in info:
            self.addLabel(QLabel(i))

    def addLabel(self, widget):
        self.vbox.addWidget(widget)