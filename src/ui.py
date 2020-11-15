import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QGridLayout, QDesktopWidget, QLineEdit
from PyQt5.QtGui import QPalette, QColor, QFont
from src.listeners import Observable, ObservableType

def setWidgetStyleSheet(widget, styles):
    concatenated = "".join([f"{style['name']}:{style['value']};" for style in styles])
    widget.setStyleSheet(concatenated)

class EditWidget(QLineEdit):
    def __init__(self):
        super().__init__()
        self.styles = []
        self.textColor = None
        self.textChangeObservable = Observable(ObservableType.TEXTENTERED)
        self.keyPressObservable = Observable(ObservableType.KEYPRESS)
        self.textChanged.connect(self.textChangeObservable.onChange)

    def configureTextColor(self, r, g, b):
        palette = QPalette()
        palette.setColor(QPalette.Text, QColor(r, g, b))
        self.setPalette(palette)

    def configureFont(self, fontName, fontSize):
        font = QFont(fontName, fontSize)
        self.setFont(font)

    def configureStyles(self, styles):
        setWidgetStyleSheet(self, styles)

    def keyPressEvent(self, event):
        self.keyPressObservable.onChange(event.key())
        super().keyPressEvent(event)

class BorderlessWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.layout = QVBoxLayout()
        self.fakeWidget = QWidget()

        self._configureLayout()

    def _configureLayout(self):
        self.fakeWidget.setLayout(self.layout)
        self.setCentralWidget(self.fakeWidget)

    def center(self, width, height):
        self.setFixedWidth(width)
        self.setFixedHeight(height)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def configureStyles(self, styles):
        setWidgetStyleSheet(self.fakeWidget, styles)

    def addWidget(self, widget):
        self.layout.addWidget(widget)

class UIManager():
    def __init__(self, app):
        self.app = app
        self.window = BorderlessWindow()
        self.editWidget = EditWidget()

    def initializeDefaultUI(self):
        globalStyles = [{ "name": "background-color", "value": "rgb(12,12,12)" }]

        self.window.center(800, 60)
        self.window.configureStyles(globalStyles)

        self.editWidget.configureFont("Cascadia Mono", 14)
        self.editWidget.configureTextColor(204, 204, 204)
        self.editWidget.configureStyles(globalStyles + [{ "name": "border", "value": "0" }])

        self.window.addWidget(self.editWidget)

    def clearText(self):
        self.editWidget.clear()

    def shutdown(self):
        self.app.quit()