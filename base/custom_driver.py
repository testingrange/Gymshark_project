from selenium import webdriver

import logging
import os
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
from custom_logger import customLogger as CL
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

class SeleniumCustomDriver():

    log = CL(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screeenshot(self, resultMessage):
        timestamp = str(time.strftime("%m%d%Y_%H%M%S"))
        screenshotName = f"{timestamp}_{resultMessage}"
        locationName = os.getcwd()+"/screenshots/"
        screenshotLocation = locationName + screenshotName
        try:
            if not os.path.exists(locationName):
                os.makedirs(locationName)
                self.log.info(f"Screenshot location {locationName} was created")
            self.driver.save_screenshot(screenshotLocation)
            self.log.info(f"Screenshot {screenshotName} was saved to screenshot location - {locationName}")
        except:
            self.log.error("### Exception occurred.")
            print_stack()


    def getByType(self, locatorType):
        locatorType = locatorType.upper()
        if locatorType == "XPATH":
            return By.XPATH
        elif locatorType == "ID":
            return By.ID
        elif locatorType == "LINK":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "CSS":
            return By.CSS_SELECTOR
        elif locatorType == "CLASS":
            return By.CLASS_NAME
        elif locatorType == "NAME":
            return By.NAME
        elif locatorType == "TAG":
            return By.TAG_NAME
        else:
            self.log.error(f"LocatorType {locatorType} has not been found")
            return False

    def getElement(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.driver.find_element(self.getByType(locatorType),locator)
                self.log.info(f"WebElement with locator - {locator} and locatorType - {locatorType} has been successfuly found.")
            else:
                self.log.info(f"Element {element} was provided")
        except:
            self.log.error(f"Either element or locator/locatorType were not correctly provided")
            print_stack()
        return element

    def getElements(self, locator="", locatorType="id"):
        elements = None
        try:
            if locator:
                elements = self.driver.find_elements(self.getByType(locatorType), locator)
                self.log.info(f"WebElements with locator - {locator} and locatorType - {locatorType} have been successfuly found.")
        except:
            self.log.error(f"Either element or locator/locatorType were not correctly provided")
            print_stack()
        return elements

    def elementPresenseCheck(self, locator, locatorType='id'):
        try:
            elementsList = self.getElements(locator, locatorType)
            if len(elementsList) > 1:
                self.log.info(f"Elements with locator - {locator} and locatorType - {locatorType} present on the screen.")
                return True
            elif len(elementsList) > 0:
                self.log.info(f"Element with locator - {locator} and locatorType - {locatorType} present on the screen.")
                return True
            else:
                self.log.error(f"Element with locator - {locator} and locatorType - {locatorType} doesn't present on the screen.")
                return False
        except:
            self.log.error(f"Exception occurred. Element with locator - {locator} and locatorType - {locatorType} doesn't present on the screen.")
            return False

    def isElementDisplayed(self, locator, locatorType='id'):
        isDisplayed = False
        try:
            element = self.getElement(locator, locatorType)
            if element.is_displayed():
                self.log.info(f"WebElement with locator - {locator} and locatorType - {locatorType} is displayed.")
            else:
                self.log.error(f"WebElement with locator - {locator} and locatorType - {locatorType} is not displayed.")
            return element.is_displayed()
        except:
            self.log.error(f"Exception occurred. WebElement with locator - {locator} and locatorType - {locatorType} is not displayed.")
            return False

    def waitForElement(self, locator, locatorType='id', timeout=15, poll=0.5):
        """Module for waiting for an element during a cirtain time - timeout"""
        element = None
        try:
            self.log.info(f"Waiting {timeout} seconds with poll_frequency - {poll} seconds for element with locator - {locator} and locatorType - {locatorType}")
            wait = WebDriverWait(self.driver, timeout, poll, ignored_exceptions=[NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException,
                                                                                 ElementNotInteractableException, NoSuchElementException])
            element = wait.until(EC.presence_of_element_located((self.getByType(locatorType), locator)))
            self.log.info(f"Element with locator - {locator} and locatorType - {locatorType} has appeared on the page")
        except:
            self.log.error(f"Exception occurred. Element with locator - {locator} and locatorType - {locatorType} has not appeared on the page")
        return element

    def elementClick(self, locator="", locatorType='id', element=None):
        try:
            if locator:
                element=self.getElement(locator, locatorType)
            element.click()
            self.log.info(f"Element {element} has been clicked on")
        except:
            self.log.error(f"Exception occurred! Element with locator - {locator} and locatorType - {locatorType} has not been found")
            print_stack()

    def sendTextToElement(self, text, locator="", locatorType='id', element=None):
        try:
            if locator:
                element=self.getElement(locator, locatorType)
            element.send_keys(text)
            self.log.info(f"{text} has been sent to the element - {element}")
        except:
            self.log.error(f"Exception occurred! Element with locator - {locator} and locatorType - {locatorType} has not been found")
            print_stack()

    def selectFromElement(self, value, valueName, locator="", locatorType="id", element=None):
        """Select item from selector.
        Select by index --> valueNum=1,
                 visible Text --> valueNum=2,
                 or value --> valueNum=3.
                 Insert corresponding value and assign corresponding number to valueName.
                 Input locator and locatorType for selector - element or element."""
        try:
            if locator:
                element=self.getElement(locator, locatorType)
                sel = Select(element)
                if valueName == 1:
                    sel.select_by_index(value)
                    self.log.info(f"Index value - {value} has been selected from selector element with locator {locator} and locatorType {locatorType}")
                elif valueName == 2:
                    sel.select_by_visible_text(value)
                    self.log.info(
                        f"Text value - {value} has been selected from selector element with locator {locator} and locatorType {locatorType}")
                elif valueName == 3:
                    sel.select_by_value(value)
                    self.log.info(
                        f"Value - {value} has been selected from selector element with locator {locator} and locatorType {locatorType}")
            else:
                self.log.error(f"Element with locator - {locator} and locatorType - {locatorType} has not been found.")
        except:
            self.log.error(f"Exception occurred! Select action cannot be performed with element with locator - {locator} and locatorType - {locatorType}")



    def getText(self, locator="", locatorType="id"):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            text = element.text
            self.log.info(f"Text of the element is {text}")
            if len(text) == 0:
                text = element.get_attribute("innerText")
                self.log.info(f"{text} of the element with locator - {locator} and locatorType - {locatorType}")
        except:
            self.log.error(f"Failed to get text on element")
            print_stack()
            text = None
        return text




