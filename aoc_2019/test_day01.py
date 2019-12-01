from day01_module import calculateFuel
from day01_module import calculateTotalModuleFuel

def test_day01_mass12():
    assert calculateFuel(12) == 2

def test_day01_mass14():
    assert calculateFuel(14) == 2

def test_day01_mass1969():
    assert calculateFuel(1969) == 654

def test_day01_mass100756():
    assert calculateFuel(100756) == 33583

def test_day01_masswithfuel14():
    assert calculateTotalModuleFuel(14) == 2

def test_day01_masswithfuel1969():
    assert calculateTotalModuleFuel(1969) == 966

def test_day01_masswithfuel100756():
    assert calculateTotalModuleFuel(100756) == 50346

