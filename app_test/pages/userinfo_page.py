from appium.webdriver.common.mobileby import MobileBy as By

from pages.base_page import BasePage


class UserinfoPage(BasePage):
    '''用户页面'''
    balance_locator = (By.CLASS_NAME, 'color_sub')

    def balance_element(self):
        return self.wait_presence_element(self.balance_locator)

    def balance_num(self):
        balance_str = self.balance_element().text[0:-1]
        return float(balance_str)