import inspect
import logging

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#@pytest.mark.usefixtures("browsersetup") #Here browsersetup in the method in the conftest.py file
@pytest.mark.usefixtures("browsersetup")

class BaseClass:

    def scriptlogging(self):
        loggerName = inspect.stack()[1][3]
        # __name captures the file name
        logger = logging.getLogger(loggerName)
        # logging parent method stores in logs file
        FileHandler = logging.FileHandler('logs.log')
        # Format of logs the parent will generate
        formattype = logging.Formatter("%(asctime)s: %(levelname)s : %(name)s: %(message)s")
        # File handler message format creation
        FileHandler.setFormatter(formattype)
        # File handler should be called in logger method
        logger.addHandler(FileHandler)
        # Set log levels
        logger.setLevel(logging.DEBUG)
        #return logger
        return logger

    def WaitforXPATH(self, xpathlocator):
    #pass #does not do anything
        wait = WebDriverWait(self.driver, 4)
        wait.until(EC.presence_of_element_located((By.XPATH, xpathlocator)))

    def scriptactions(self):
        WebDriverWait(self.driver, 4)
        actions = ActionChains(self.driver)
        return actions

    def scriptwaitfornextaction(self):
        WebDriverWait(self.driver, 2)

