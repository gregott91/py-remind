from src.parsing.tokenizer import tokenize
from PyQt5.QtCore import Qt
from src.parsing.token_type import TokenType
from src.tasks.text_task import TextTask

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
            self._saveTokens()

    # todo i need error handling in this whole chain
    def _saveTokens(self):
        task = self._getTask()
        task.save(self.taskRepository)

    def _getTask(self):
        textTokens = list(self._getMatchingToken(TokenType.TEXT))

        if len(textTokens) == len(self.tokens) and len(textTokens) == 1:
            return TextTask(textTokens[0].text)

    def _getMatchingToken(self, tokenType):
        for token in self.tokens:
            if token.tokenType == tokenType:
                yield token