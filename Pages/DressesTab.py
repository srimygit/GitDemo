import time

import pytest
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.ElementIdentifiers import PageElements
from Locators.eleidentifiers import Locators
from utilities.baseclass import BaseClass


class testdresses(BaseClass):


    def __init__(self, driver):
        self.driver = driver

    #WomenTabClick = (By.XPATH, "//span[text() = 'Women']")  # self.getLocators["WomenTabClick"]
    DressesWomenTabClick = (By.XPATH, PageElements.DRTAB)

    def drtab(self):
        DressTabCLicking = self.driver.find_elements(*testdresses.DressesWomenTabClick)
        DressTabCLicking[1].click()
        # Logging to click on Dresses Tab
        mainscripttestcaselogs = self.scriptlogging()
        mainscripttestcaselogs.info("Clicking on the Dresses tab")
        self.scriptwaitfornextaction()

        DressesShown = self.driver.find_elements_by_xpath("//div[@class='product-container']")
        # Logging to confirm item was found on the page
        mainscripttestcaselogs = self.scriptlogging()
        mainscripttestcaselogs.info("Dress found on the page")
        DressesOptions = self.scriptactions()
        DressesOptions.move_to_element(DressesShown[0]).perform()
        # Logging when hovering over the dress
        mainscripttestcaselogs = self.scriptlogging()
        mainscripttestcaselogs.info("Hovering over the dress item")

        self.scriptwaitfornextaction()
        DressesShown[0].find_element_by_xpath("//span[text()='Add to cart']").click()
        #Logging to confirm item was added to cart
        mainscripttestcaselogs = self.scriptlogging()
        mainscripttestcaselogs.info("Dress added to shopping cart")

        time.sleep(2)
        #self.scriptwaitfornextaction()
        checkoutbutton = DressesShown[0].find_element_by_xpath("//div[contains(@class,'layer_cart_cart')]/div[@class='button-container']/a/span[contains(text(),'checkout')]")
        DressesOptions.move_to_element(checkoutbutton).perform()

        checkoutbutton.click()
        # Logging to confirm item was checked-out from cart
        mainscripttestcaselogs = self.scriptlogging()
        mainscripttestcaselogs.info("Dress checked out from shopping cart")

        #Wait once cart summary is loaded
        self.scriptwaitfornextaction()

        ShoppingCost = self.driver.find_element_by_xpath("//table[@id='cart_summary']/tfoot/tr[7]/td[2]/span")
        mainscripttestcaselogs.info("Shopping cost is:" +str(ShoppingCost.text))
