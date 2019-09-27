from appium.webdriver.common.mobileby import MobileBy as By


class LoginLocator:
    phone = (By.NAME, 'phone')
    pwd = (By.NAME, 'password')
    submit = (By.XPATH, "//button[contains(@class, 'btn-special')]")

class investLocator:
    pass

class UserinfoLocator:
    pass

class HomeLocator:
    welcome_enter_button_locator = (By.ID, "com.xxzb.fenwoo:id/btn_start")

