import pytest

@pytest.mark.positive
def test_creative_booking_positive():
    print("This is pytest case")
    assert 1 -1 == 2

@pytest.mark.regression
def test_creative_booking_negative_1():
    print("This is pytest case")
    assert 1 + 1 == 2


@pytest.mark.negative
def test_creative_booking_negative_2():
    print("This is pytest case")
    assert 1 + 1 == 2