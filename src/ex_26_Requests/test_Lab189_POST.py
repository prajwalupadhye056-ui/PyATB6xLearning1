import pytest
import allure
import requests

@allure.title("TC # Create Booking CRUD positive.")
@allure.description("Verify the create Booking! : ")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_path = base_url + base_path

    headers = {

        "Content-Type": "application/json"
    }

    payload = {

        "firstname": "Pooja",
        "lastname": "Khanna",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }


    response_data = requests.post(url=full_path, headers=headers, json=payload)
    print(response_data.text)
    assert response_data.status_code == 200

    # Booking_ID > 0 and firstname  == "Jim"
