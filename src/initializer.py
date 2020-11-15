import sys
from src.listeners import ExitListener, TextListener
from src.db.connections import DBManager, DBOptions
from src.db.repositories import TaskRepository, TaskTypeRepository
from src.ui import UIManager
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QGridLayout, QDesktopWidget, QLineEdit

def configureUI():
    manager = UIManager()
    manager.initializeDefaultUI()

    return manager

def configureSubscriptions(widget, keypressListener, textListener):
    keypressListener.subscribe(widget.keyPressObservable)
    textListener.subscribe(widget.textChangeObservable)
    textListener.subscribe(widget.keyPressObservable)

def configureListeners(app, uiManager):
    options = DBOptions('sqlite:///local.db', True)
    dbManager = DBManager(options)
    dbManager.initialize()

    taskTypeRepo = TaskTypeRepository(dbManager)
    taskRepo = TaskRepository(dbManager, taskTypeRepo)

    exitListener = ExitListener(app)
    textListener = TextListener(taskRepo, uiManager)

    return {
        "exitListener": exitListener,
        "textListener": textListener
    }