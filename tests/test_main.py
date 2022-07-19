import py
import pytest

from actions.main import sum

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (3, -3, 0)])
def test_main(a: float, b: float, expected: float) -> None:
    assert sum(a, b) == expected
    