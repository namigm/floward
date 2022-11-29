from selenium.webdriver.common.by import By
from locators.main_locators import Locators



class BaseObject(Locators):

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def selector_gen(selector):
        selector_dict = {"css": By.CSS_SELECTOR,
                         "xpath": By.XPATH,
                         "linktext":By.LINK_TEXT
                         }
        return selector_dict[selector]

    def element(self, selector, locator_name):
        return self.driver.find_element(self.selector_gen(selector), self.select_locator(locator_name))