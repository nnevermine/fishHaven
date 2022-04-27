from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QGroupBox, QGridLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic, QtGui
import sys


class Dashboard(QMainWindow):

    def __init__(self, allFish=None):
        super().__init__()
        self.fished = allFish
        print(self.fished[0].getId())
        self.initUI()
    def initUI(self):

        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()         # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.grid = QGridLayout()
        for i in range(0,5):
            for j in range(0,3):
                self.grid.addWidget(QPushButton(str(i)+str(j)),i,j)

        self.widget.setLayout(self.grid)
       


        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(80, 90, 1280, 720)
        self.setWindowTitle('Dashboard')
        self.show()

        return