import sys
from src.listeners import KeypressListener, TextEnteredListener
from src.db.connections import DBManager, DBOptions
from src.db.repositories import TaskRepository, TaskTypeRepository
from src.ui import UIManager
from src.parsing.tokens import TokenRepository
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QGridLayout, QDesktopWidget, QLineEdit

def configureUI(app):
    manager = UIManager(app)
    manager.initializeDefaultUI()

    return manager

def configureSubscriptions(widget, keypressListener, textListener):
    keypressListener.subscribe(widget.keyPressObservable)
    textListener.subscribe(widget.textChangeObservable)

def configureListeners(uiManager):
    options = DBOptions('sqlite:///local.db', True)
    dbManager = DBManager(options)
    dbManager.initialize()

    taskTypeRepo = TaskTypeRepository(dbManager)
    taskRepo = TaskRepository(dbManager, taskTypeRepo)
    tokenRepo = TokenRepository()

    keypressListener = KeypressListener(uiManager, tokenRepo, taskRepo)
    textListener = TextEnteredListener(tokenRepo)

    return {
        "keypressListener": keypressListener,
        "textListener": textListener
    }