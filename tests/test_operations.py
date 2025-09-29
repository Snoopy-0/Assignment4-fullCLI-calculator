import pytest
from app.operation import AddOperation, SubtractOperation, MultiplyOperation, DivideOperation

@pytest.mark.parametrize(
    "op,a,b,expected",
    [
        (AddOperation(), 2, 3, 5),
        (SubtractOperation(), 5, 10, -5),
        (MultiplyOperation(), -2, 4, -8),
        (DivideOperation(), 10, 2, 5),
        (DivideOperation(), 7.5, 2.5, 3.0),
    ],
)
def test_operations_compute(op, a, b, expected):
    assert op.compute(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        DivideOperation().compute(1, 0)
