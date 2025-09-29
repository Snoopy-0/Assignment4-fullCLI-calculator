import pytest
from app.calculation import CalculationFactory, Calculation, UnknownOperation

@pytest.mark.parametrize(
    "key,a,b,expected",
    [
        ("add", 2, 3, 5),
        ("+", 2, 3, 5),
        ("plus", 2, 3, 5),
        ("sub", 5, 2, 3),
        ("-", 5, 2, 3),
        ("mul", 3, 4, 12),
        ("*", 3, 4, 12),
        ("times", 3, 4, 12),
        ("div", 8, 4, 2),
        ("/", 8, 4, 2),
        ("divide", 8, 4, 2),
    ],
)
def test_factory_create_and_calculation_result(key, a, b, expected):
    calc = CalculationFactory.create(key, a, b)
    assert isinstance(calc, Calculation)
    assert calc.result() == expected
    s = str(calc)
    assert str(a) in s and str(b) in s and str(expected) in s

def test_factory_unknown_operation():
    with pytest.raises(UnknownOperation):
        CalculationFactory.create("pow", 2, 3)
