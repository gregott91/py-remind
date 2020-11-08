from src.parsing.tokenizer import tokenize

class TextListener():
    def subscribe(self, observable):
        observable.subscribe(self.textEntered)

    def textEntered(self, text):
        tokens = tokenize(text)