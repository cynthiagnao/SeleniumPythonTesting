import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("Firstname is "+ getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys("12345")
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.getCheckbox().click()
        homePage.getStatus().click()
        homePage.submitForm().click()
        alertText = homePage.getSuccessMessage().text
        print(alertText)
        assert "Success" in alertText
        time.sleep(2)
        homePage.getInputbox().send_keys("hello again")
        homePage.getInputbox().clear()

        time.sleep(3)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self,request):
        return (request).param


