import pytest

from day04_module import hasDouble, neverDecrease, isValidPassword, doubleNotInLargeGroup

testDoublesData = [
    ('111111', True),
    ('223450', True),
    ('123789', False)
]

@pytest.mark.parametrize("password, hasDoubleConfirmation", testDoublesData)
def test_day04_hasDouble(password, hasDoubleConfirmation):
    assert hasDouble(password) == hasDoubleConfirmation

testNeverDecreaseData = [
    ('111111', True),
    ('223450', False),
    ('123789', True)
]

@pytest.mark.parametrize("password, neverDecreaseConfirmation", testNeverDecreaseData)
def test_day04_neverDecrease(password, neverDecreaseConfirmation):
    assert neverDecrease(password) == neverDecreaseConfirmation

testValidData = [
    ('111111', True),
    ('223450', False),
    ('123789', False)
]

@pytest.mark.parametrize("password, isValidConfirmation", testValidData)
def test_day04_validPassword(password, isValidConfirmation):
    assert isValidPassword(password) == isValidConfirmation

testDoubleNotInLargeGroupData = [
    ('112233', True),
    ('123444', False),
    ('111122', True) #existe um par de 22 que é o par de duplo mesmo com o 1 passando de 2
]

@pytest.mark.parametrize("password, doubleNotInLargeGroupConfirmation", testDoubleNotInLargeGroupData)
def test_day04_doubleNotInLargeGroup(password, doubleNotInLargeGroupConfirmation):
    assert doubleNotInLargeGroup(password) == doubleNotInLargeGroupConfirmation

