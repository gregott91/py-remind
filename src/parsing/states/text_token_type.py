from src.parsing.tokens.text_token import TextToken
from src.parsing.token_text_position import TokenTextPosition

class TextTokenType:
    def match(self, text):
        return TextToken(TokenTextPosition(0, len(text)))