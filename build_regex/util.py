from __future__ import annotations
from dataclasses import dataclass
from . import Regex

__all__ = [
    "exactly",
    "oneOrMore",
    "Letter",
    "Not",
    "tab",
    "At",
    "chars",
    "tab",
    "digit",
    "word_char",
    "whitespace",
    "word_break",
    "new_line",
    "cr",
    "vtab",
    "form_feed",
    "backspace",
    "word_boundry",
    "char",
]

def exactly(_input: str) -> Regex:
    """Creates a pattern for matching the exact string provided.

    Escapes the characters `.`, `[`, `]`, `(`, `)`, `^`, `$`, `{`, `}`, `|`.
    """

    special_chars = ".[]()$^{}|"
    result = ""
    for char in _input:
        if char in special_chars:
            result += f"\\{char}"
        else:
            result += char

    return Regex(result)

def oneOrMore(_input: str | Regex) -> Regex:
    reg = Regex(f"(?:{_input})")
    reg.expr += "+"
    return reg

def noneOrMore(_input: str | Regex) -> Regex:
    reg = Regex(f"(?:{_input})")
    reg.expr += "*"
    return reg

class Letter:
    lowercase: Regex = Regex("[a-z]")
    uppercase: Regex = Regex("[A-Z]")

    @staticmethod
    def negate() -> Letter:
        letter = Letter()
        letter.lowercase = Regex("[^a-z]")
        letter.uppercase = Regex("[^A-Z]")
        return letter

def tab() -> Regex:
    return Regex("\t")

def digit() -> Regex:
    return Regex("\\d")

def word_char() -> Regex:
    return Regex("\\w")

def whitespace() -> Regex:
    return Regex("\\s")

def word_break() -> Regex:
    return Regex("\\b")

def new_line() -> Regex:
    return Regex("\n")

def cr() -> Regex:
    return Regex("\r")

def vtab() -> Regex:
    return Regex("\v")

def form_feed() -> Regex:
    return Regex("\f")

def backspace() -> Regex:
    return Regex("[\b]")

def word_boundry() -> Regex:
    return Regex("\b")

def char() -> Regex:
    return Regex(".")

def word() -> Regex:
    return Regex("\\b\\w+\\b")

@dataclass
class Not:
    letter: Letter = Letter.negate()
    digit: Regex = Regex("\\D")
    word_char: Regex = Regex("\\W")
    whitespace: Regex = Regex("\\S")
    word_boundry: Regex = Regex("\\B")

    @staticmethod
    def chars(_input: str) -> Regex:
        return Regex(f"[^{_input}]")

class At:
    def __init__(self, expr: Regex) -> None:
        self.regex = expr
    
    @property
    def line_start(self) -> Regex:
        if not self.regex.expr.startswith("^"):
            return Regex(f"^{self.regex}")
        return self.regex

    @property
    def line_end(self) -> Regex:
        if not self.regex.expr.endswith("$"):
            return Regex(f"{self.regex}$")
        return self.regex
    
def chars(_input: str):
    return Regex(f"[{_input}]")