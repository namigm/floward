import pytest
from utilities.readproperties import ReadConfig
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Chrome(service=Service(GeckoDriverManager().install()))
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture()
def base_fix(setup):
    driver = setup
    driver.get(ReadConfig.get_url())
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()


def pytest_configure(config):
    config._metadata['Project name'] = 'floward'
    config._metadata['Tester'] = 'NamigM'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)