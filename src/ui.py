import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QDesktopWidget, QLineEdit, QListWidget, QTabWidget
from PyQt5.QtGui import QPalette, QColor, QFont
from src.listeners import Observable, ObservableType

def setWidgetStyleSheet(widget, styles):
    concatenated = "".join([f"{style[0]}:{style[1]};" for style in styles])
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

class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self._configureTabs()
    
    def _configureTabs(self):
        self.todoListTab = QListWidget()
        self.reminderTab = QListWidget()
        
        self.addTab(self.todoListTab,"To Dos")
        self.addTab(self.reminderTab,"Reminders")
        self.setStyleSheet("margin: 0")
        self.tabBar().setStyleSheet("QTabBar::tab { width: 300px; height: 30px; }")
        self.tabBar().setFont(QFont("Segoe UI", 14))

class UIManager():
    def __init__(self, app):
        self.app = app
        self.window = BorderlessWindow()
        self.editWidget = EditWidget()
        self.tabWidget = TabWidget()
        self.initialHeight = 60
        self.expandedHeight = 300

    def initializeDefaultUI(self):
        self.editWidget.configureFont("Cascadia Mono", 14)
        self.editWidget.configureTextColor(204, 204, 204)
        self.editWidget.configureStyles([
                [ "background-color", "rgb(12,12,12)" ],
                [ "padding-left", "8px" ],
                [ "padding-right", "8px" ],
                [ "border", "0" ],
                [ "height", f"{self.initialHeight}px" ]
            ])

        self.tabWidget.hide()

        self.window.center(800, self.initialHeight)
        self.window.addWidget(self.editWidget)
        self.window.addWidget(self.tabWidget)

    def clearText(self):
        self.editWidget.clear()

    def shutdown(self):
        self.app.quit()

    def hideList(self):
        self.window.setHeight(self.initialHeight)
        self.tabWidget.hide()

    def showList(self):
        self.window.setHeight(self.expandedHeight)
        self.tabWidget.show()

    def show(self):
        self.window.show()