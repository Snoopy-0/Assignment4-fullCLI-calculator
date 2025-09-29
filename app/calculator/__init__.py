"""Calculator REPL and helpers.

This module implements a small command-line calculator with a REPL, input
validation (LBYL and EAFP), a calculation history, and special commands:
help, history, and exit.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Tuple, Union
import re

from ..calculation import Calculation, CalculationFactory, UnknownOperation

@dataclass
class CalculatorState:
    history: List[Calculation] = field(default_factory=list)

def help_text() -> str:
    """Return help text for the REPL."""
    operations = ", ".join(sorted(set(CalculationFactory.valid_operations())))
    return (
        "Commands:\n"
        "  help           Show this message\n"
        "  history        Show calculation history\n"
        "  exit           Quit the program\n\n"
        "Operations (type one of):\n  " + operations + "\n\n"
        "Usage example:\n  > add\n  Enter first number: 2\n  Enter second number: 3\n  Result: 5\n"
    )

# --- Input validation helpers ---
_FLOAT_RE = re.compile(r"^[+-]?(?:\d+(?:\.\d*)?|\.\d+)$")

def parse_float_lbyl(s: str) -> float:
    """LBYL: look before you leap.
    Validate with a regex before converting. Raises ValueError if the text
    is not a float-looking string.
    """
    if not _FLOAT_RE.match(s.strip()):
        raise ValueError(f"Not a valid number: {s!r}")
    return float(s)

def parse_float_eafp(s: str) -> float:
    """EAFP: easier to ask forgiveness than permission.
    Try to convert directly and catch exceptions.
    """
    try:
        return float(s)
    except Exception as exc:  # broad on purpose to show EAFP
        raise ValueError(f"Not a valid number: {s!r}") from exc

def _format_history(state: CalculatorState) -> str:
    if not state.history:
        return "(no calculations yet)"
    lines = [f"{idx+1}. {str(c)}" for idx, c in enumerate(state.history)]
    return "\n".join(lines)

# Return type: (status, payload). status in {"ok","help","history","exit","error"}
def parse_and_execute(command: str, state: CalculatorState,
                      a: float | None = None, b: float | None = None) -> Tuple[str, Union[str, float]]:
    cmd = command.strip().lower()
    if cmd in {"help", "h", "?"}:
        return ("help", help_text())
    if cmd in {"history"}:
        return ("history", _format_history(state))
    if cmd in {"exit", "quit", "q"}:
        return ("exit", "Goodbye!")

    # Otherwise, treat it as an operation via the factory
    if a is None or b is None:  # pragma: no cover
        # Interactive prompting path
        while True:
            try:
                a = parse_float_eafp(input("Enter first number: "))  # pragma: no cover
                break
            except ValueError as e:
                print(e)  # pragma: no cover
        while True:
            try:
                b = parse_float_eafp(input("Enter second number: "))  # pragma: no cover
                break
            except ValueError as e:
                print(e)  # pragma: no cover

    assert a is not None and b is not None  # for type checkers

    try:
        calc = CalculationFactory.create(cmd, a, b)
    except UnknownOperation as e:
        return ("error", str(e))

    # Create & evaluate
    try:
        result = calc.result()
    except ZeroDivisionError as e:
        return ("error", str(e))
    state.history.append(calc)
    return ("ok", result)

def run_repl() -> None:  # pragma: no cover
    """Start the interactive REPL."""
    state = CalculatorState()
    print("Professional-Grade CLI Calculator")  # pragma: no cover
    print(help_text())  # pragma: no cover
    while True:  # pragma: no cover
        command = input("> ").strip().lower()
        status, payload = parse_and_execute(command, state)
        if status == "exit":
            print(payload)  # pragma: no cover
            break
        elif status == "ok":
            print(f"Result: {payload}")  # pragma: no cover
        else:
            print(payload)  # pragma: no cover


def unused_placeholder() -> None:
    """Demonstrates coverage exceptions for intentionally uncovered code."""
    pass  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover - entry point
    run_repl()
