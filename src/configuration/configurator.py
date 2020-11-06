import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QGridLayout, QDesktopWidget, QLineEdit
from src.ui.borderless_window import BorderlessWindow
from src.ui.edit_widget import EditWidget

def fun(state):
    print(state)

def configureUI(app, keypressListener, textListener):
    window = BorderlessWindow()
    window.center(800, 60)

    widget = EditWidget()
    widget.configureFont("Cascadia Mono", 14)
    widget.configureTextColor(204, 204, 204)
    widget.configureStyles([
        { "name": "background-color", "value": "rgb(12,12,12)" },
        { "name": "padding-left", "value": "8px" },
        { "name": "padding-right", "value": "8px" },
        { "name": "border", "value": "0" }
    ])

    _configureSubscriptions(widget, keypressListener, textListener)

    window.setWidget(widget)

    return window

def _configureSubscriptions(widget, keypressListener, textListener):
    keypressListener.subscribe(widget.keyPressObservable)
    textListener.subscribe(widget.textChangeObservable)