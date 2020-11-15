import sys
from src.listeners import ExitListener, TextListener
from src.db.connections import DBManager, DBOptions
from src.db.repositories import TaskRepository
from src.ui import BorderlessWindow, EditWidget
from src.initializer import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QGridLayout, QDesktopWidget, QLineEdit

app = QApplication([])

uiManager = configureUI()
listeners = configureListeners(app, uiManager)
configureSubscriptions(uiManager.editWidget, listeners["exitListener"], listeners["textListener"])

uiManager.window.show()

sys.exit(app.exec_())