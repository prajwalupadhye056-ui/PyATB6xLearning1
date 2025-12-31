import pytest
import allure
import requests

@allure.title("TC#1- Create Booking CRUD positive.")
@allure.description("Verify the create booking : ")
@pytest.mark.crud
def test_get_booking_positive_tc1():
    url = "https://restful-booker.herokuapp.com/booking/190"
    response_data= requests.get(url=url)
    assert response_data.status_code ==200

@allure.title("Verify the Get Request of Restful Booker with Invalid ID")
@allure.description("This Testcase check Booking -1 and verify the response ")
@pytest.mark.negative
def test_get_request():
    url_get = "https://restful-booker.herokuapp.com/booking/-1"
    response_data= requests.get(url=url_get)
    assert response_data.status_code ==404