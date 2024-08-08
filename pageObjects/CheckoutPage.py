from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    #Declare Constructor
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)
        #self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")

    def getCardFooters(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)
        #self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")



