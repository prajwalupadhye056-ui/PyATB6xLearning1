import pytest
import allure
import requests


@allure.title("TC # Verify 2-2 == 0.")
@allure.description("This is BASIC Math Test : ")
@pytest.mark.positive
def test_basic_math():
    assert 2 - 2 == 0


@allure.title("TC#2 Verify that 3-3 is equal to 0")
@allure.description("This is smoke testcase ")
@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0


@pytest.mark.skip(reason= "Not working skip it")
def test_sub3():
    assert 0 - 0 != 0