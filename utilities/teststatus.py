from Gymshark_project.base.custom_driver import SeleniumCustomDriver as SD
from utilities.custom_logger import customLogger as CL
import logging
from traceback import print_stack

class TestStatus(SD):
    """
    Class to use for validate testing in test classes and not to
    skip tests until all test passed or failed.
    """

    log = CL(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        """

        :param result:
        :param resultMessage:
        :return:
        """
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("Verification successfully" + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("Verification failed" + resultMessage)
                    self.screeenshot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("Verification failed" + resultMessage)
                self.screeenshot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("Exception occurred")
            self.screeenshot(resultMessage)
            print_stack()


    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)
        if 'FAIL' in self.resultList:
            self.log.error(f'{testName} ### TEST FAILED')
            self.resultList.clear()
            assert False == True
        else:
            self.log.info(f'{testName} ### TEST SUCCESSFUL')
            self.resultList.clear()
            assert True == True
            
