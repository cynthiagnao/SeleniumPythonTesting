import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass

#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        #checkoutPage = CheckoutPage(self.driver)
        log.info("Getting all the card titles")
        cards = checkoutPage.getCardTitles()
        #cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")

        confirmPage = ConfirmPage(self.driver)

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooters()[i].click()
                #self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()

        confirmPage = checkoutPage.checkOutItems()
        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        log.info("Entering country name as ind")

        confirmPage.confirmCheckOut().click()
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        confirmPage.typeCountry() #.send_keys("ind")
        #self.driver.find_element(By.ID, "country").send_keys("ind")

        self.verifyLinkPresence("India")
        '''WebDriverWait(self.driver, 10).until(
            confirmPage.checkPresenceOfElementIndia()
            #EC.presence_of_element_located((By.LINK_TEXT, "India"))
        )'''

        confirmPage.selectCountry().click()
        #self.driver.find_element(By.LINK_TEXT, "India").click()

        confirmPage.agreeTermsConditions().click()
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        confirmPage.submitOrder().click()
        #self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        textMatch = confirmPage.getAlertMessage().text
        #textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        log.info("Text received from application is" + textMatch)

        assert ("Success! Thank you!" in textMatch) #add error in the text to generate error
        time.sleep(3)





