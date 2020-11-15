from src.parsing.tokenizer import tokenize
from PyQt5.QtCore import Qt
from src.parsing.tokens import TokenType
from src.tasks import TextTask
from src.parsing.processing import saveTokens
from enum import Enum

class ExitListener():
    def __init__(self, app):
        self.app = app
    
    def subscribe(self, observable):
        observable.subscribe(self.keyChanged)

    def keyChanged(self, key):
        if key == Qt.Key_Escape:
            self.app.quit()

class TextListener():
    def __init__(self, taskRepository, uiManager):
        self.taskRepository = taskRepository
        self.uiManager = uiManager

    def subscribe(self, observable):
        if observable.observableType == ObservableType.KEYPRESS:
            observable.subscribe(self.keyPressed)
        elif observable.observableType == ObservableType.TEXTENTERED:
            observable.subscribe(self.textEntered)

    def textEntered(self, text):
        self.tokens = tokenize(text)

    def keyPressed(self, key):
        if key in [Qt.Key_Enter, Qt.Key_Return]:
            saveTokens(self.taskRepository, self.tokens)
            self.uiManager.clearText()


class ObservableType(Enum):
    TEXTENTERED = 1
    KEYPRESS = 2

class Observable:
    def __init__(self, observableType):
        super().__init__()
        self.observableType = observableType
        self.subscriptions = []

    def subscribe(self, fun):
        self.subscriptions.append(fun)

    def onChange(self, state):
        [x(state) for x in self.subscriptions]