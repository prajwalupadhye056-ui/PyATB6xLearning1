import pytest

@pytest.mark.positive
def test_method2():
    print("This is pytest case")
    assert True == False

@pytest.mark.regression
def test_method3():
    print("This is pytest case")
    assert 5 == 5