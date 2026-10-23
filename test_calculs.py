from calculs import addition, soustraction, multiplication, division


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_soustraction():
    assert soustraction(5, 3) == 2
    assert soustraction(1, 1) == 0
    assert soustraction(0, 0) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 5) == 0

def test_division():
    assert division(6, 3) == 2
    assert division(-4, 2) == -2
    assert division(0, 1) == 0

    try:
        division(5, 0)
    except ValueError as e:
        assert str(e) == "Division par zéro n'est pas autorisée."