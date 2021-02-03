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


