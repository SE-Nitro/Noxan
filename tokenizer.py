import enum
import re
from codepage import codepage


class TokenType(enum.Enum):
    """Class for all Tokens"""

    NUMBER = "number"
    STRING = "string"
    FUNCTION = "function"


class RegEx(enum.Enum):
    """Regex helping class for IsType"""

    NUMBER = r"\d"
    IGNORE_TOKEN = r" "


class IsType:
    """Class to check which token a string is"""

    @staticmethod
    def number(char: str):
        return bool(re.match(RegEx.NUMBER.value, char))

    @staticmethod
    def function(char: str):
        return char in codepage

    @staticmethod
    def ignore_token(char: str):
        return bool(re.match(RegEx.IGNORE_TOKEN.value, char))


class Indicator:
    STRING_CHAR = ' " '


class Token:
    """Token class"""

    def __init__(self, name: TokenType, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Token(name={self.name}, value={repr(self.value)})"  # {self.value} for debugging


def tokenize(text: str) -> list[Token]:
    tokens = []
    current_number = False
    number = ""
    string_start = False
    string = ""

    for char in text:
        if not IsType.number(char):
            if current_number:
                tokens.append(Token(TokenType.NUMBER, int(number)))
                current_number = False
                number = ""
            elif char == Indicator.STRING_CHAR and string_start:
                string += char

        if IsType.ignore_token(char):
            continue

        elif IsType.function(char):
            tokens.append(Token(TokenType.FUNCTION, char))

        elif IsType.number(char):
            if not current_number:
                current_number = True
                number += char
            else:
                number += char

        elif char == Indicator.STRING_CHAR:
            if not string_start:
                string_start = True
            else:
                tokens.append(Token(TokenType.STRING, char))

    if current_number:
        tokens.append(Token(TokenType.NUMBER, int(number)))

    return tokens


if __name__ == "__main__":
    print(tokenize("+7 59*89 / 207"))
    print(tokenize("+1 +3 4"))
    print(tokenize("2 \"test\""))
