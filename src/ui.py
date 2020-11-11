import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QGridLayout, QDesktopWidget, QLineEdit
from PyQt5.QtGui import QPalette, QColor, QFont
from src.listeners import Observable

class EditWidget(QLineEdit):
    def __init__(self):
        super().__init__()
        self.styles = []
        self.textColor = None
        self.textChangeObservable = Observable()
        self.keyPressObservable = Observable()
        self.textChanged.connect(self.textChangeObservable.onChange)

    def configureTextColor(self, r, g, b):
        palette = QPalette()
        palette.setColor(QPalette.Text, QColor(r, g, b))
        self.setPalette(palette)

    def configureFont(self, fontName, fontSize):
        font = QFont(fontName, fontSize)
        self.setFont(font)

    def configureStyles(self, styles):
        concatenated = "".join([f"{style['name']}:{style['value']};" for style in styles])
        self.setStyleSheet(concatenated)

    def keyPressEvent(self, event):
        self.keyPressObservable.onChange(event.key())
        super().keyPressEvent(event)
class BorderlessWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

    def center(self, width, height):
        self.setFixedWidth(width)
        self.setFixedHeight(height)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def setWidget(self, widget):
        self.setCentralWidget(widget)