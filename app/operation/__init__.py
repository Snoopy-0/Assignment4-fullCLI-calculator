"""Operations module.
Defines the abstract class: Operation and concrete arithmetic operations.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class Operation(ABC):
    """Abstract base class for arithmetic operations."""
    name: str = "op"
    symbol: str = "?"

    @abstractmethod
    def compute(self, a: float, b: float) -> float:
        """Return the result of applying the operation to a and b."""
        raise NotImplementedError  # pragma: no cover

    def __repr__(self) -> str:  # pragma: no cover - trivial repr
        return f"{self.__class__.__name__}(name={self.name!r}, symbol={self.symbol!r})"


class AddOperation(Operation):
    name = "add"
    symbol = "+"

    def compute(self, a: float, b: float) -> float:
        return a + b


class SubtractOperation(Operation):
    name = "sub"
    symbol = "-"

    def compute(self, a: float, b: float) -> float:
        return a - b


class MultiplyOperation(Operation):
    name = "mul"
    symbol = "*"

    def compute(self, a: float, b: float) -> float:
        return a * b


class DivideOperation(Operation):
    name = "div"
    symbol = "/"

    def compute(self, a: float, b: float) -> float:
        if b == 0:
            # EAFP style: raise and let caller handle
            raise ZeroDivisionError("division by zero")
        return a / b


__all__ = [
    "Operation",
    "AddOperation",
    "SubtractOperation",
    "MultiplyOperation",
    "DivideOperation",
]
