from src.parsing.token_type import TokenType

class TextToken:
    @property
    def tokenType(self):
        return TokenType.TEXT
    
    def __init__(self, textPosition, text):
        self.textPosition = textPosition
        self.text = text

    def transformText(self):
        return None