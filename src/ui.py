import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QDesktopWidget, QLineEdit, QListWidget, QLayout
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
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.fakeWidget.setStyleSheet("height: 0px;")
        self.fakeWidget.setLayout(self.layout)
        self.setCentralWidget(self.fakeWidget)

    def center(self, width, height):
        self.setFixedWidth(width)
        self.setHeight(height)
        
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def configureStyles(self, styles):
        setWidgetStyleSheet(self.fakeWidget, styles)

    def addWidget(self, widget):
        self.layout.addWidget(widget)

    def setHeight(self, height):
        self.setFixedHeight(height)

class UIManager():
    def __init__(self, app):
        self.app = app
        self.window = BorderlessWindow()
        self.editWidget = EditWidget()
        self.listWidget = QListWidget()
        self.initialHeight = 60

    def initializeDefaultUI(self):
        self.editWidget.configureFont("Cascadia Mono", 14)
        self.editWidget.configureTextColor(204, 204, 204)
        self.editWidget.configureStyles([
                { "name": "background-color", "value": "rgb(12,12,12)" },
                { "name": "padding-left", "value": "8px" },
                { "name": "padding-right", "value": "8px" },
                { "name": "border", "value": "0" },
                { "name": "height", "value": f"{self.initialHeight}px"}
            ])

        self.listWidget.hide()

        self.window.center(800, self.initialHeight)
        self.window.addWidget(self.editWidget)
        self.window.addWidget(self.listWidget)

    def clearText(self):
        self.editWidget.clear()

    def shutdown(self):
        self.app.quit()

    def hideList(self):
        self.window.setHeight(60)
        self.listWidget.hide()

    def showList(self):
        self.window.setHeight(200)
        self.listWidget.show()

    def show(self):
        self.window.show()