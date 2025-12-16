import pytest
import allure
import requests

@allure.title("TC # Create Booking CRUD positive.")
@allure.description("Verify the create Booking! : ")
#@pytest.mark.crud
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
    assert response_data.status_code == 200

    response_data_json= response_data.json()
    print(response_data)
   # assert response_data.status_code == 200

    # Booking_ID > 0 and firstname  == "Jim"
    bookingId = response_data_json["bookingid"]
    firstname= response_data_json["booking"]["firstname"]
    print(bookingId)
    print(firstname)

    assert bookingId is not None
    assert bookingId > 0
    assert type(bookingId)  == int

    assert firstname == "Jim"
    assert type(firstname) == str

    lastname =response_data_json["booking"]["lastname"]
    totalprice= response_data_json["booking"]["totalprice"]
    depositpaid = response_data_json["booking"]["depositpaid"]

    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid ==True

  #https: //jsonpathfinder.com
    checkin = response_data_json["booking"]["bookingdates"]["checkin"]
    checkout= response_data_json["booking"]["bookingdates"]["checkout"]

    assert checkin == "2018-01-01"
    assert checkout =="2019-01-01"


    time = response_data.elapsed.total_seconds()
    assert time < 3


    @allure.title("TC#2- Create Booking CRUD Ngative")
    @allure.description("Verify that invalid payload Booking is not")
    @pytest.mark.crud
    def test_create_booking_negative_tc1():
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking"
        Url = base_url + base_path

        headers = {
            "Content-Type": "application/json"
        }

        json_payload = {}  # Empty payload for negative test

        response = requests.post(url=Url, headers=headers, json=json_payload)

        assert response.status_code == 500
        assert response.text == "Internal Server Error"
