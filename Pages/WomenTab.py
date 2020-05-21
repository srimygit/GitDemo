import time

import pytest
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import Locators
# from Locators import eleidentifiers
# from Locators.eleidentifiers import locators
from Locators.ElementIdentifiers import PageElements
from Locators.eleidentifiers import Locators
from utilities.baseclass import BaseClass


class testwomen(BaseClass):


    def __init__(self, driver):
        self.driver = driver

    #WomenTabClick = (By.XPATH, "//span[text() = 'Women']")  # self.getLocators["WomenTabClick"]
    WomenTabClick = (By.XPATH, PageElements.WTC)
    WomenLabelCheck = (By.XPATH, PageElements.WLC)
    WomenPageExpandOptions = (By.XPATH, PageElements.WPEO)

    def wt(self):

         #Create logger object
         testlogs = self.scriptlogging()

         #Identify the Women Menu Bar Item
         WomenHoverMenu = self.driver.find_element(*testwomen.WomenLabelCheck)

         # Hover over Women Menu bar
         hovermenu = self.scriptactions()
         hovermenu.move_to_element(WomenHoverMenu).perform()

         #CLick on the "T-Shirts" link on the hover
         TShirts = self.driver.find_element_by_xpath("//a[text()='T-shirts']")
         #Wait for TShirts to be interactable(Required for Firefox)
         time.sleep(2)
         #CLick on the TShirts link
         TShirts.click()

         #Wait for all checkboxes to load
         self.scriptactions()

         # Click on the "Small" size checkbox shown on the page
         smallcheckbox = self.driver.find_element_by_xpath("//input[@id='layered_id_attribute_group_1']")
         status = smallcheckbox.is_selected()
         #If checkbox "Small" under "Size" is not checked, then check it
         if status == False:
             testlogs.info("Checking the small size shirt checkbox")
             smallcheckbox.click()
             testlogs.info("After checking the checkbox, continuing with the test case")
         else:
             testlogs.info("small size shirt checkbox already checked. continuing with the test case")

         #Wait after clicking
         self.scriptwaitfornextaction()

         #Verify that the label "Catalog" is shown
         Catalog = self.driver.find_element_by_xpath("//p[text()='Catalog']")
         if Catalog.text=="CATALOG":
             testlogs.info("Catalog section found. Execute next set of statements")
         else:
             testlogs.error("Catalog section not found. Executing next set of statements")

         #assert Catalog.text =="CATALOG"
         testlogs.info("Catalog display result:" +Catalog.text)
         # LoginUserID = self.getUserCred[0]
         #Wait before clicking
         self.scriptwaitfornextaction()

         #Select from T-Shirt dropdown
         sortdrop = self.driver.find_element_by_xpath("//select[@id='selectProductSort']")
         sortdropdown  = Select(sortdrop)
         #Sorty by lowest price
         sortdropdown.select_by_visible_text("Price: Lowest first")
         # Wait after selecting the dropdown value
         self.scriptwaitfornextaction()

         #CLick on the Women Menu Tab
         self.driver.find_element(*testwomen.WomenLabelCheck).click()
         wait = WebDriverWait(self.driver, 2)
         WomenMenuItem = self.driver.find_element(*testwomen.WomenLabelCheck)
         wait.until(EC.presence_of_element_located, (By.XPATH, WomenMenuItem))
         result = WomenMenuItem.is_displayed()
         # Capture logs
         testlogs.info("WomenMenubar display result:" +str(result))

         ExpandButtons = self.driver.find_elements(*testwomen.WomenPageExpandOptions)

         topoptionresult = ExpandButtons[0].is_displayed()
         ExpandButtons[0].click()
         time.sleep(5)
         testlogs.info("Tops option display result:" +str(topoptionresult))

    # def wtclick(self, WomenTabClickLocator):
    #     #
    #     WTCLoc = '"' +WomenTabClickLocator+ '"'
    #     print(WTCLoc)
    #     time.sleep(2)
    #     self.driver.find_element(*testwomen.WomenLabelCheck).click()
    #     #self.driver.find_element(By.XPATH, WTCLoc).click()





