import sys
import keyboard
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QGridLayout, QDesktopWidget, QLineEdit
from src.ui.borderless_window import BorderlessWindow

def configureUI(app):
    window = BorderlessWindow()
    window.center(800, 60)

    editWidget = QLineEdit()

    palette = QPalette()
    palette.setColor(QPalette.Text, QColor(204, 204, 204))
    editWidget.setPalette(palette)

    font = QFont("Cascadia Mono", 14)
    editWidget.setFont(font)

    editWidget.setStyleSheet("""
    background-color: rgb(12,12,12);
    padding-left: 8px;
    padding-right: 8px;
    border: 0;
    """)

    window.setCentralWidget(editWidget)

    return window

def temp(app):
    window = BorderlessWindow()
    window.center(800, 60)

    editWidget = QLineEdit()

    palette = QPalette()
    palette.setColor(QPalette.Text, QColor(204, 204, 204))
    editWidget.setPalette(palette)

    font = QFont("Cascadia Mono", 14)
    editWidget.setFont(font)

    editWidget.setStyleSheet("""
    background-color: rgb(12,12,12);
    padding-left: 8px;
    padding-right: 8px;
    border: 0;
    """)

    window.setCentralWidget(editWidget)

    window.show()

def configureHotKeys(app):
    keyboard.add_hotkey('alt+x', lambda:temp(app))