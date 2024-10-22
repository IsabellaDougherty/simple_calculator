import pytest
import math
from calculator.simple_calculator import (
    squareNums,
    triNums,
    lazyCaterer,
    magicSquares,
    cubeNums,
    circNum,
    surfArea,
)
@pytest.mark.parametrize("n, expected", [
    (2, 4),
    (3, 9),
    (-4, 16),
])
def test_squareNums(n, expected):
    assert squareNums(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1,1),
    (3,6),
    (5,15),
])

def test_triNums(n, expected):
    assert trinums(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 2),
    (2, 4),
    (3, 7),
])

def test_lazyCaterer(n, expected):
    assert lazyCaterer(n) == expected

@pytest.mark.parametrize("n, expected", [
    (3, 15),
    (4, 34),
    (5, 65),
])

def test_magicSquares(n, expected):
    assert magicSquares(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 4),
    (3, 9),
])

def test_cubeNum(n, expected):
    assert cubeNum(n) == expected

@pytest.mark.parametrize("r, expected", [
    (1, 2 * math.pi * 1),
    (2, 2 * math.pi * 2),
    (3, 2 * math.pi * 3),
])

def test_circNum(n, expected):
    assert circNum(n) == expected

@pytest.mark.parametrize("r, expected", [
    (1, 4 * math.pi * 1**2),
    (2, 4 * math.pi * 2**2),
    (3, 4 * math.pi * 3**2),
])

def test_surfArea(n, expected):
    assert surfArea(n) == expected
