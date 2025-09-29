"""Calculation objects and a CalculationFactory.

A class: Calculation holds operands and a class: Operation instance.
The class: CalculationFactory creates a calculation from a user-friendly
operation string (e.g., "add", "+").
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Iterable
from .. import operation as ops


@dataclass(frozen=True)
class Calculation:
    a: float
    b: float
    op: ops.Operation

    def result(self) -> float:
        return self.op.compute(self.a, self.b)

    def __str__(self) -> str:
        return f"{self.a} {self.op.symbol} {self.b} = {self.result()}"


class UnknownOperation(ValueError):
    pass


class CalculationFactory:
    """Create class: Calculation objects based on user input."""

    # Map normalized keys to concrete operation classes
    _op_map: Dict[str, type[ops.Operation]] = {
        "add": ops.AddOperation,
        "+": ops.AddOperation,
        "plus": ops.AddOperation,
        "sub": ops.SubtractOperation,
        "-": ops.SubtractOperation,
        "minus": ops.SubtractOperation,
        "mul": ops.MultiplyOperation,
        "*": ops.MultiplyOperation,
        "times": ops.MultiplyOperation,
        "x": ops.MultiplyOperation,
        "div": ops.DivideOperation,
        "/": ops.DivideOperation,
        "divide": ops.DivideOperation,
    }

    @classmethod
    def valid_operations(cls) -> Iterable[str]:
        return sorted(set(cls._op_map.keys()))

    @classmethod
    def create(cls, op_key: str, a: float, b: float) -> Calculation:
        key = op_key.strip().lower()
        try:
            op_cls = cls._op_map[key]
        except KeyError as exc:
            raise UnknownOperation(f"Unknown operation: {op_key!r}") from exc
        return Calculation(a=a, b=b, op=op_cls())


__all__ = ["Calculation", "CalculationFactory", "UnknownOperation"]
