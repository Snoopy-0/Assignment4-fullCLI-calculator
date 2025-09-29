# Professional-Grade CLI Calculator

A modular, professional-grade **command-line calculator** written in Python.  
This project demonstrates clean architecture, error handling, testing, and continuous integration with GitHub Actions.

---

## Features

- **REPL Interface**: Interactive Read-Eval-Print Loop for continuous user interaction.
- **Arithmetic Operations**: Addition, subtraction, multiplication, division.
- **User Prompts**: Enter operation + operands, get immediate feedback.
- **Input Validation**:  
  - *LBYL* (Look Before You Leap) validation with regex.  
  - *EAFP* (Easier to Ask Forgiveness than Permission) with exception handling.
- **Error Handling**: Graceful handling of invalid inputs and division by zero.
- **Calculation Management**:  
  - `CalculationFactory` creates operations.  
  - Session history is tracked and viewable.  
  - Special commands: `help`, `history`, `exit`.

---

## Project Structure

```
app/
  __init__.py
  calculator/
    __init__.py     # REPL & main logic
    __main__.py     # Entry point (so `python -m app.calculator` works)
  calculation/
    __init__.py     # Calculation + factory
  operation/
    __init__.py     # Arithmetic operations
tests/
  conftest.py
  test_operations.py
  test_calculations.py
  test_repl_and_validation.py
requirements.txt
README.md
.github/workflows/python-ci.yml
```

---

## Getting Started

### 1. Clone & Setup
```bash
git clone git@github.com:Snoopy-0/Assignment4-fullCLI-calculator.git
cd Assignment4-fullCLI-calculator
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 2. Run the Calculator
```bash
python -m app.calculator.__init__
```

#### Example session
```
Professional-Grade CLI Calculator
Commands:
  help           Show this message
  history        Show calculation history
  exit           Quit the program

Operations (type one of):
  add, sub, mul, div, +, -, *, /

Usage example:
  > add
  Enter first number: 2
  Enter second number: 3
  Result: 5

> history
1. 2.0 + 3.0 = 5.0
> exit
Goodbye!
```

---

## Testing

uses pytest and pytest-cov to get 100% test coverage.

Run all tests:
```bash
python -m pytest --cov=app --cov-branch -q
coverage report --fail-under=100
```

Run a specific test file:
```bash
pytest tests/test_operations.py -q
```

Generate HTML coverage report:
```bash
coverage html
open htmlcov/index.html   # macOS
```

---

## Requirements

- Python **3.11+** (tested on 3.13)
- Dependencies:
  - `pytest`
  - `pytest-cov`

Install with:
```bash
pip install -r requirements.txt
```

---

## Author
- Gianvito Tribuzio
- Developed as part of CS 601 – Assignment 4
- Demonstrates professional Python project setup, testing, and CI
