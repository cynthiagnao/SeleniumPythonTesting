import pytest
import inspect
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



@pytest.mark.usefixtures("setup")
class BaseClass:
    #pass #do nothing

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        # this object is responsible to log everything, it will capture the test file name
        logger = logging.getLogger(loggerName)  # logger is an object responsible of printing   #WHAT TO PRINT

        fileHandler = logging.FileHandler('logfile.log')  # indicate where it should print   #WHERE TO PRINT
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # HOW TO PRINT (FORMAT)
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)  # Debug will be skipped

        return  logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)