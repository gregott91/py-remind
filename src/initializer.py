import sys
from src.listeners import ExitListener, TextListener
from src.db.connections import DBManager, DBOptions
from src.db.repositories import TaskRepository, TaskTypeRepository
from src.ui import BorderlessWindow, EditWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QGridLayout, QDesktopWidget, QLineEdit

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

    window.setWidget(widget)

    return {
        "window": window,
        "widget": widget
    }

def configureSubscriptions(widget, keypressListener, textListener):
    keypressListener.subscribe(widget.keyPressObservable)
    textListener.subscribe(widget.textChangeObservable, widget.keyPressObservable)

def configureListeners(app):
    options = DBOptions('sqlite:///local.db', True)
    dbManager = DBManager(options)
    dbManager.initialize()

    taskTypeRepo = TaskTypeRepository(dbManager)
    taskRepo = TaskRepository(dbManager, taskTypeRepo)

    exitListener = ExitListener(app)
    textListener = TextListener(taskRepo)

    return {
        "exitListener": exitListener,
        "textListener": textListener
    }