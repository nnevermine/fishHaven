from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel

class FishFrame(QGroupBox):
    
    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.addInfo(info)

    def addInfo(self, info):
        for i in info:
            self.addLabel(QLabel(i))

    def addLabel(self, widget):
        self.vbox.addWidget(widget)