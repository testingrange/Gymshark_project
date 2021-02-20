import pytest
from selenium import webdriver
from Gymshark_project.pages.main.main_page import MainPage as MP

def getWebDriverInstance(browser):

    """
    Get WebDriver Instance based on the browser configuration

    :return:'WebDriver Instance'
    """
    baseURL = "https://www.gymshark.com/"
    if browser == "iexplorer":
        driver = webdriver.Ie()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    mp = MP(driver)

    # Setting Driver Implicit Time out for An Element
    driver.implicitly_wait(3)
    # Maximize the window
    driver.maximize_window()
    # Loading browser with App URL
    driver.get(baseURL)
    mp.closeCookiesWindow()
    return driver

@pytest.fixture(scope="class")
def mainPageSetUp(request, browser):
    print("\n================================\nONE TIME !!! BEFORE All the methods\n================================")

    driver = getWebDriverInstance(browser)

    # lp.login("michaelsole75@gmail.com", "MS75gl")
    # 4266 8416 1160 6102 -> Your card is declined. Please contact your Bank/Card Issuer for more information.
    # if browser == 'firefox':
    #     #     baseURL = "https://courses.letskodeit.com/"
    #     #     driver = webdriver.Firefox()
    #     #     driver.implicitly_wait(6)
    #     #     driver.maximize_window()
    #     #     driver.get(baseURL)
    #     #     print("Running test on FF")
    #     # else:
    #     #     baseURL = "https://courses.letskodeit.com/"
    #     #     driver = webdriver.Chrome()
    #     #     driver.implicitly_wait(6)
    #     #     driver.maximize_window()
    #     #     driver.get(baseURL)
    #     #     print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("\n================================\nONE TIME AFTER !!! All the methods\n================================")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

