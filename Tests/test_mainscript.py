#Packages for Explicit Wait
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
#Package to import time
import time

#from Locators import eleidentifiers
from Locators.eleidentifiers import Locators
from Pages.WomenTab import testwomen
from Pages.DressesTab import testdresses
from utilities.baseclass import BaseClass

class Testpracticesite(BaseClass):

    def test_womentab(self):#, getLocators):
        tw = testwomen(self.driver)
        tw.wt()
        mainscripttestcaselogs = self.scriptlogging()
        mainscripttestcaselogs.info("Women Tab Test Execution completed")

    def test_dressestab(self):
        dr = testdresses(self.driver)
        dr.drtab()
        mainscripttestcaselogs = self.scriptlogging()
        mainscripttestcaselogs.info("Dresses Tab Test Execution completed")

    def test_developbranch1(self):
        print("This is the develop branchhhhh")

        print("Second change in develop branch")

    print("All test cases completed")
    print("Done for the day")
    print("Goodbye Srinath Prabhakar")
    print("Do you want to start again?")
    print("Yes I do")
    
    print("New Changes in Practice Automation project")


    #def test_dressestab(self):


        #tw.wt(getLocators["WomenTabClick"])
        #Click on the Women tab
        #tw.wt()
    # Dictionary declaration
    #@pytest.fixture(params=locators.getTestData())
    # @pytest.fixture(params=Locators.test_Locators)
    # def getLocators(self, request):
    #      return request.param


