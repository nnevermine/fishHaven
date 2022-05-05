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
        pixmap = QPixmap('./assets/images/sprites/local-pond/1.png')
        label = QLabel(self)

        if info[3].lower() == "sick-salmon":
            pixmap = QPixmap('./assets/images/sprites/local-pond/1.png')
        elif info[3].lower() == "peem":
            pixmap = QPixmap('./assets/images/sprites/foreign-pond/1.png')
        elif info[3].lower() == "dang":
            pixmap = QPixmap('./assets/images/sprites/dang.png')
        elif info[3].lower() == "pla":
            pixmap = QPixmap('./assets/images/sprites/plafish.png')

        pixmap = pixmap.scaled(low_rez)
        label.setPixmap(pixmap)
        self.addLabel(label)

        self.addLabel(QLabel("ID: " + str(info[0])))
        self.addLabel(QLabel("State: " + str(info[1])))
        self.addLabel(QLabel("Status: " + str(info[2])))
        self.addLabel(QLabel("Genesis: " + str(info[3])))
        self.addLabel(QLabel("Lifetime: " + str(info[4])))


    def addLabel(self, widget):
        self.vbox.addWidget(widget)