from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize

class PondFrame(QGroupBox):
    
    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)
        self.addInfo(info)

    def addInfo(self, info):
        label = QLabel(self)

        self.addLabel(label)

        self.addLabel(QLabel("Pond Name: " + str(info[0])))
        self.addLabel(QLabel("Amount of Fishes: " + str(info[1])))
        for i in info[2]:
            self.addLabel(QLabel(str(i)))

    def addLabel(self, widget):
        self.vbox.addWidget(widget)