from selenium.webdriver.remote.mobile import Mobile

from appium.webdriver.common.mobileby import MobileBy as By

from pages.base_page import BasePage


class NavPage(BasePage):
    '''底部导航栏'''
    user_locator = (By.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"我\")")
    bid_locator = (By.ANDROID_UIAUTOMATOR, "com.xxzb.fenwoo:id/btn_login")
    login_button_locator = (By.ID, "new UiSelector().resourceId('com.xxzb.fenwoo:id/btn_login')")

    @property
    def user_elem(self):
        return self.wait_click_element(self.user_locator)

    def click_user_my(self):
        self.wait_click_element(self.user_locator).click()

