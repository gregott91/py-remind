class TextListener():
    def subscribe(self, observable):
        observable.subscribe(self.textEntered)

    def textEntered(self, text):
        print(text)