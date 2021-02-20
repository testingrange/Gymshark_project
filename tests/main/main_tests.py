from Gymshark_project.pages.main.main_page import MainPage as MP
from Gymshark_project.utilities.teststatus import TestStatus as TS
import pytest
import unittest
from ddt import ddt, data, unpack
from Gymshark_project.utilities.read_data import getCSVData


@pytest.mark.usefixtures("mainPageSetUp")
@ddt
class MainPageTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, mainPageSetUp):
        self.mp = MP(self.driver)
        self.ts = TS(self.driver)

    def closeCookieWindow(self):
        self.mp.closeCookiesWindow()

    @data(*getCSVData("C:\\Users\\S4etovodov\\PycharmProjects\\preparationForWork\\Gymshark_project\\tests\\main\\countrySelectorData.csv"))
    @unpack
    def testSelector(self, countryCode, countryName, confirm):
        self.mp.selectCountryFromList(countryCode, confirm)
        result = self.mp.verifySelectorOption(countryName)
        self.ts.markFinal("Test country selector", result, countryName)
