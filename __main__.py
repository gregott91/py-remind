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

listeners = configureListeners(app)
ui = configureUI(app, listeners["exitListener"], listeners["textListener"])
configureSubscriptions(ui["widget"], listeners["exitListener"], listeners["textListener"])

ui["window"].show()

sys.exit(app.exec_())