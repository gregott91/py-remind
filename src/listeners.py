from src.parsing.tokenizer import tokenize
from PyQt5.QtCore import Qt
from src.parsing.tokens import TokenType
from src.tasks import TextTask
from src.parsing.processing import saveTokens
from enum import Enum

class KeypressListener():
    def __init__(self, uiManager, tokenRepository, taskRepository):
        self.uiManager = uiManager
        self.tokenRepository = tokenRepository
        self.taskRepository = taskRepository
    
    def subscribe(self, observable):
        observable.subscribe(self.keyChanged)

    def keyChanged(self, key):
        if key == Qt.Key_Escape:
            self.uiManager.shutdown()
        elif key in [Qt.Key_Enter, Qt.Key_Return]:
            saveTokens(self.taskRepository, self.tokenRepository.tokens)
            self.tokenRepository.clearTokens()
            self.uiManager.clearText()
        elif key == Qt.Key_Down:
            self.uiManager.showList()
        elif key == Qt.Key_Up:
            self.uiManager.hideList()

class TextEnteredListener():
    def __init__(self, tokenRepository):
        self.tokenRepository = tokenRepository

    def subscribe(self, observable):
        observable.subscribe(self.textEntered)

    def textEntered(self, text):
        self.tokenRepository.setTokens(tokenize(text))


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