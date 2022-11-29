class Locators:

    @staticmethod
    def select_locator(locator_key):
        loc = {
            "countryUK_xpath": '//img[@alt="United Kingdom"]',

            "categoryFV_lt": 'Flowers in Vases',

            "flowerJMoments_xpath": '//img[@alt="Joyful Moments"]',

            "addCardJMoments_css": '.fui-mt-8',

            "closeBtn_xpath": '//button[@data-testid="TestId__CloseBtn"]',

            "card_css": 'img.fui-rounded'
        }
        return loc[locator_key]
