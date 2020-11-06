from parsing.states.text_token_type import TextTokenType
from parsing.tokens.reminder_time_token import ReminderTimeToken
from parsing.reminder_unit import ReminderUnit
from parsing.token_text_position import TokenTextPosition
from parsing.reminder_time import ReminderTime

class ReminderTimeTokenType:
    @property
    def nextStates(self):
        return [
            TextTokenType()
        ]

    def match(self, text):
        # match conditions are:
        # if it starts with "in" or a number
        words = text.split()
        rawValue = None
        rawUnit = None

        if words[0] == "in":
            rawValue = words[1]
            rawUnit = words[2]
        else:
            rawValue = words[0]
            rawUnit = words[1]

        if rawValue.isnumeric():
            unit = self._match_unit(rawUnit)
            value = int(rawValue)

            if unit is not None:
                start = 0
                end =  (text.find(rawUnit, 0, len(text)) - 1) + len(rawUnit)
                textPosition = TokenTextPosition(start, end)
                
                time = ReminderTime(value, unit)

                return ReminderTimeToken(textPosition, time)

    def _match_unit(self, unit):
        matchers = [
            (['seconds', 'second', 'secs', 'sec', 'sc', 's'], ReminderUnit.SECOND),
            (['minutes', 'minute', 'mins', 'min', 'mn', 'm'], ReminderUnit.MINUTE),
            (['hours', 'hour', 'hrs', 'hr', 'h'], ReminderUnit.HOUR),
            (['days', 'day', 'd'], ReminderUnit.DAY)
        ]

        for matcher in matchers:
            if self._does_match(unit, matcher[0]):
                return matcher[1]

        return None


    def _does_match(self, unit, matchers):
        return unit in matchers