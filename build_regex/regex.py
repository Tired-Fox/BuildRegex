from __future__ import annotations
import re
from re import Pattern
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import At

__all__ = [
    "Regex",
    "build_regex",
]

class Regex:    
    def __init__(self, expr: Regex | str | None = None):
        self.expr = str(expr or "")
        
    @property
    def at(self) -> At:
        from . import At
        return At(self)

    def then(self, obj: Regex | str) -> Regex:
        """Add passed in pattern to the current pattern as is.

        Example:
            x -> xy
        """
        from . import exactly

        if isinstance(obj, str):
            self.expr += str(exactly(obj))
        if isinstance(obj, Regex):
            self.expr += str(obj)
        return self

    def Or(self, obj: Regex | str) -> Regex:
        """Create an alternate matching pattern for the current regex pattern.

        Example:
            x -> x|y
        """
        from . import exactly
        
        if isinstance(obj, str):
            self.expr += "|" + str(exactly(obj))
        if isinstance(obj, Regex):
            self.expr += "|" + str(obj)
        return self

    def any(self) -> Regex:
        self.expr = f"(?:{self.expr})*"
        return self

    def at_least(self, _min: int) -> Regex:
        self.expr = f"(?:{self.expr}){{{_min}}}"
        return self
    
    def between(self, _min: int, _max: int) -> Regex:
        self.expr = f"(?:{self.expr}){{{_min},{_max}}}"
        return self
    
    def times(self, times: int) -> Regex:
        self.expr = f"(?:{self.expr}){{{times}}}"
        return self
    
    def optional(self) -> Regex:
        self.expr = f"(?:{self.expr})?"
        return self
    
    def after(self, _input: str | Regex) -> Regex:
        self.expr = f"(?<={_input})" + self.expr
        return self
        
    def before(self, _input: str | Regex) -> Regex:
        self.expr = self.expr + f"(?={_input})"
        return self
        
    def not_after(self, _input: str | Regex) -> Regex:
        self.expr = f"(?<!{_input})" + self.expr
        return self
        
    def not_before(self, _input: str | Regex) -> Regex:
        self.expr = self.expr + f"(?!{_input})" 
        return self

    def group(self) -> Regex:
        self.expr = f"(?:{self.expr})"
        return self
        
    def capture(self, name: str = ""):
        if name != "":
            self.expr = f"(?P<{name}>{self.expr})"
        else:
            self.expr = f"({self.expr})"
        return self
            
    def ref(self, name: str | int = 1):
        if isinstance(name, str):
            self.expr += f"\\k<{name}>"
        else:
            self.expr += f"\\{name}"
        return self

    def compile(self) -> Pattern:
        """Returns a compiled re.Pattern using re.compile. This allows a user
        to use all re's regex methods on the constructed pattern."""

        return re.compile(str(self))

    def __str__(self) -> str:
        return self.expr

def build_regex(_input: str | Regex):
    return re.compile(str(_input))
