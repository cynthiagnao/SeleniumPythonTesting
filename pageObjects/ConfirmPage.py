from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ConfirmPage:

    #Declare Constructor
    def __init__(self, driver):
        self.driver = driver

    checkOutOrder = (By.XPATH, "//button[@class='btn btn-success']")
    country = (By.ID, "country")
    countryLetters = ("ind")
    countryIndia = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    alertMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def confirmCheckOut(self):
        return self.driver.find_element(*ConfirmPage.checkOutOrder)
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']")

    def typeCountry(self):
        return self.driver.find_element(*ConfirmPage.country).send_keys(*ConfirmPage.countryLetters)
        #self.driver.find_element(By.ID, "country").send_keys("ind")

    def checkPresenceOfElementIndia(self):
        return EC.presence_of_element_located((ConfirmPage.countryIndia))
        #EC.presence_of_element_located((By.LINK_TEXT, "India"))

    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.countryIndia)
        #self.driver.find_element(By.LINK_TEXT, "India")

    def agreeTermsConditions(self):
        return self.driver.find_element(*ConfirmPage.checkBox)
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def submitOrder(self):
        return self.driver.find_element(*ConfirmPage.submit)
        #self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")

    def getAlertMessage(self):
        return self.driver.find_element(*ConfirmPage.alertMessage)
        #self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']")
