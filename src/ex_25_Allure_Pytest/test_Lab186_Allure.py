import pytest
import allure

@allure.title("Verify that create booking with invalid data is working.")
@allure.description("This test case check for negative ")
@pytest.mark.negative

def test_create_booking_negative_1():
    print("test1")
    assert 1-1 == 2

@allure.title("Verify that create booking is working.")
@allure.description("Verify that the create booking in the future of this function")
@pytest.mark.positive
def test_create_booking_positive():
    print("test2")
    assert 1 + 1 == 2

@allure.title("Verify that create booking is working.")
@allure.description("Verify that the create booking in the future of this function")
@pytest.mark.positive
def test_create_booking_positive_2():
    print("test2")
    assert 1 + 1 == 2