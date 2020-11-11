from enum import Enum

class TokenType(Enum):
    TEXT = 1
    REMINDER_TIME = 2

class TokenTextPosition:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class ReminderUnit(Enum):
    SECOND = 1
    MINUTE = 2
    HOUR = 3
    DAY = 4

class ReminderTimeToken:
    @property
    def tokenType(self):
        return TokenType.REMINDER_TIME

    def __init__(self, textPosition, reminderTime):
        self.textPosition = textPosition
        self.reminderTime = reminderTime
    
    def transformText(self):
        return None

class TextToken:
    @property
    def tokenType(self):
        return TokenType.TEXT
    
    def __init__(self, textPosition, text):
        self.textPosition = textPosition
        self.text = text

    def transformText(self):
        return None

class ReminderTime:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit