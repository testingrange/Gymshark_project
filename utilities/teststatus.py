from Gymshark_project.base.custom_driver import SeleniumCustomDriver as SD
from utilities.custom_logger import customLogger as CL
import logging

class TestStatus(SD):

    log = CL(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):