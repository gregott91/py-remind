from src.parsing.tokens import TokenType
from src.tasks import TextTask

# todo i need error handling in this whole chain
def saveTokens(taskRepository, tokens):
    task = _getTask(tokens)
    task.save(taskRepository)

def _getTask(tokens):
    textTokens = list(_getMatchingToken(tokens, TokenType.TEXT))

    if len(textTokens) == len(tokens) and len(textTokens) == 1:
        return TextTask(textTokens[0].text)

def _getMatchingToken(tokens, tokenType):
    for token in tokens:
        if token.tokenType == tokenType:
            yield token