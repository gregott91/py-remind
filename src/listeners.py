from src.parsing.tokenizer import tokenize
from PyQt5.QtCore import Qt
from src.parsing.tokens import TokenType
from src.tasks import TextTask
from src.parsing.processing import saveTokens

class ExitListener():
    def __init__(self, app):
        self.app = app
    
    def subscribe(self, observable):
        observable.subscribe(self.keyChanged)

    def keyChanged(self, key):
        if key == Qt.Key_Escape:
            self.app.quit()

class TextListener():
    def __init__(self, taskRepository):
        self.taskRepository = taskRepository

    def subscribe(self, textObservable, keyObservable):
        textObservable.subscribe(self.textEntered)
        keyObservable.subscribe(self.keyPressed)

    def textEntered(self, text):
        self.tokens = tokenize(text)

    def keyPressed(self, key):
        if key in [Qt.Key_Enter, Qt.Key_Return]:
            saveTokens(self.taskRepository, self.tokens)

class Observable:
    def __init__(self):
        super().__init__()
        self.subscriptions = []

    def subscribe(self, fun):
        self.subscriptions.append(fun)

    def onChange(self, state):
        [x(state) for x in self.subscriptions]