from Gymshark_project.base.custom_driver import SeleniumCustomDriver as SD
from Gymshark_project.utilities.custom_logger import customLogger as CL
import logging

class MainPage(SD):
    log = CL(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver


    #Locators
    _selectCountryBtn = "//div[@id='app-header']/div[2]/div/div/div[5]" #xpath
    _countrySelector = "//select[@name='country']" #xpath
    _closeSelectWindow = "//button[@aria-label='close']" #xpath
    _confirmSelectBtn = "//button[contains(.,'Confirm')]" #xpath

    #Locators for tests verification

    def openSelectCountryWindow(self):
        self.elementClick(self._selectCountryBtn, "xpath")

    def selectCountryFromSelector(self, countryCode):
        self.selectFromElement(countryCode, 2, self._countrySelector, "xpath")

    def clickSelConfirmBtn(self):
        self.elementClick(self._confirmSelectBtn, "xpath")

    def closeSelectCountryWindow(self):
        self.elementClick(self._closeSelectWindow, "xpath")

    def verifySelectorOption(self, data):
        return data == self.getText(self._selectCountryBtn, "xpath")

    def selectCountryFromList(self, countryCode):
        self.openSelectCountryWindow()
        self.selectCountryFromSelector(countryCode)
        self.clickSelConfirmBtn()
