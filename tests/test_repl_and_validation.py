import pytest
from app.calculator import (
    CalculatorState,
    parse_float_lbyl,
    parse_float_eafp,
    parse_and_execute,
    help_text,
)

def test_parse_float_lbyl_accepts_valid():
    assert parse_float_lbyl("3.14") == 3.14
    assert parse_float_lbyl("-2") == -2.0
    assert parse_float_lbyl("+.5") == 0.5

@pytest.mark.parametrize("bad", ["", "abc", "--1", "1.2.3", " 1. 2 "])
def test_parse_float_lbyl_rejects_invalid(bad):
    with pytest.raises(ValueError):
        parse_float_lbyl(bad)

@pytest.mark.parametrize("text,expected", [("2", 2.0), ("-0.25", -0.25)])
def test_parse_float_eafp(text, expected):
    assert parse_float_eafp(text) == expected

def test_parse_and_execute_flow_and_history():
    state = CalculatorState()
    status, payload = parse_and_execute("add", state, 2, 3)
    assert status == "ok" and payload == 5
    status, payload = parse_and_execute("mul", state, 5, 2)
    assert status == "ok" and payload == 10
    status, payload = parse_and_execute("history", state)
    assert status == "history" and "1." in payload and "2." in payload

def test_parse_and_execute_commands_and_errors():
    state = CalculatorState()
    status, payload = parse_and_execute("pow", state, 2, 3)
    assert status == "error" and "Unknown operation" in payload
    status, payload = parse_and_execute("div", state, 1, 0)
    assert status == "error" and "division by zero" in payload
    status, payload = parse_and_execute("help", state)
    assert status == "help" and "Commands:" in payload
    status, payload = parse_and_execute("exit", state)
    assert status == "exit"

def test_empty_history_message():
    state = CalculatorState()
    status, payload = parse_and_execute('history', state)
    assert status == 'history' and '(no calculations yet)' in payload

def test_parse_float_eafp_invalid():
    with pytest.raises(ValueError):
        parse_float_eafp('not-a-number')
