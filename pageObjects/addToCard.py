from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_locators import Locators
from baseObject.baseObject import BaseObject


class AddToCard(BaseObject):

    def select_county(self):
        self.element('xpath', 'countryUK_xpath').click()

    def category_fv(self):
        self.element('linktext', "categoryFV_lt").click()

    def add_jmoments(self):
        self.driver.implicitly_wait(5)
        self.element('xpath', 'flowerJMoments_xpath').click()
        self.switch_handle_1()
        self.element('css', 'addCardJMoments_css').click()

    def switch_handle_1(self):
        child = self.driver.window_handles[1]
        self.driver.switch_to.window(child)

    def close_cart_window(self):
        WebDriverWait(self.driver, 20). \
            until(EC.element_to_be_clickable((self.selector_gen('xpath'),
                                              Locators.select_locator('closeBtn_xpath'))))
        self.element('xpath', 'closeBtn_xpath').click()

    def check_cart_jm(self):
        self.select_county()
        self.category_fv()
        self.add_jmoments()
        self.close_cart_window()
        element = self.element('css', 'card_css').get_attribute("alt")
        assert element == 'Joyful Moments'
