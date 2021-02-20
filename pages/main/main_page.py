from Gymshark_project.base.custom_driver import SeleniumCustomDriver as SD
from Gymshark_project.utilities.custom_logger import customLogger as CL
import logging

class MainPage(SD):
    log = CL(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver

    #Variables

    confirm = "Confirm"

    #Locators
    _selectCountryBtn = "//div[@id='app-header']/div[2]/div/div/div[5]" #xpath
    _countrySelector = "//select[@name='country']" #xpath
    _closeSelectWindow = "//button[@aria-label='close']" #xpath
    _confirmSelectBtn = "//button[contains(.,'{}')]" #xpath
    _closeBtnCookies = "//div[@id='onetrust-close-btn-container']/button[@aria-label='Close']" #xpath
    _refreshPageBtn = "//a[contains(.,'Refresh Page')]"

    #Locators for tests verification
    def closeCookiesWindow(self):
        cookieWindow = self.waitForElement(self._closeBtnCookies, "xpath")
        self.elementClick(element=cookieWindow)

    def openSelectCountryWindow(self):
        countryselector = self.waitForElement(self._selectCountryBtn, "xpath")
        #self.elementClick(self._selectCountryBtn, "xpath")
        self.elementClick(element=countryselector)

    def selectCountryFromSelector(self, countryCode):
        if not self.isElementDisplayed(self._countrySelector, "xpath"):
            self.waitForElement(self._countrySelector, "xpath")
        self.selectFromElement(countryCode, 3, self._countrySelector, "xpath")

    def clickSelConfirmBtn(self, confirm):
        self.elementClick(self._confirmSelectBtn.format(confirm), "xpath")

    def closeSelectCountryWindow(self):
        self.elementClick(self._closeSelectWindow, "xpath")

    def verifySelectorOption(self, data):
        return data == self.getText(self._selectCountryBtn, "xpath")

    def selectCountryFromList(self, countryCode, confirm=""):
        self.openSelectCountryWindow()
        self.selectCountryFromSelector(countryCode)
        self.clickSelConfirmBtn(confirm)
