from src.parsing.token_type import TokenType

class ReminderTimeToken:
    @property
    def tokenType(self):
        return TokenType.REMINDER_TIME

    def __init__(self, textPosition, reminderTime):
        self.textPosition = textPosition
        self.reminderTime = reminderTime
    
    def transformText(self):
        return None