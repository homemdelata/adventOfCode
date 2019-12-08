import pytest

from day04_module import hasDouble, neverDecrease, isValidPassword

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

@pytest.mark.parametrize("password, hasDoubleConfirmation", testNeverDecreaseData)
def test_day04_neverDecrease(password, hasDoubleConfirmation):
    assert neverDecrease(password) == hasDoubleConfirmation

testValidData = [
    ('111111', True),
    ('223450', False),
    ('123789', False)
]

@pytest.mark.parametrize("password, hasDoubleConfirmation", testValidData)
def test_day04_validPassword(password, hasDoubleConfirmation):
    assert isValidPassword(password) == hasDoubleConfirmation


