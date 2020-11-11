from src.parsing.token_types import ReminderTimeTokenType, TextTokenType

def _crawl_states(text, nextStates):
    for state in nextStates:
        token = state.match(text)

        if token is not None:
            end = token.textPosition.end

            if len(text) == end or len(state.nextStates) == 0 or state.nextStates is None:
                return [token]
            else:
                remainingText = text[end:len(text)]
                remainingTokens = _crawl_states(remainingText, state.nextStates)

                tokens = [token] + remainingTokens

                return tokens

def tokenize(text):
    beginStates = [
        ReminderTimeTokenType(),
        TextTokenType()
    ]

    states = _crawl_states(text, beginStates)

    return states