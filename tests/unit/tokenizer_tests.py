import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../..")

import unittest
from src.parsing.tokenizer import tokenize
from src.parsing.tokens import ReminderUnit, TokenType

class TokenizerTests(unittest.TestCase):
    def test_tokenize_recognizesReminder(self):
        tokens = tokenize("in 30 min call Liz")

        self.assertEqual(tokens[0].tokenType, TokenType.REMINDER_TIME)
        self.assertEqual(tokens[0].reminderTime.value, 30)
        self.assertEqual(tokens[0].reminderTime.unit, ReminderUnit.MINUTE)
        self.assertEqual(tokens[0].textPosition.start, 0)
        self.assertEqual(tokens[0].textPosition.end, 8)

        self.assertEqual(tokens[1].tokenType, TokenType.TEXT)
        self.assertEqual(tokens[1].textPosition.start, 0)
        self.assertEqual(tokens[1].textPosition.end, 10)


if __name__ == '__main__':
    unittest.main()