from appium.webdriver.common.mobileby import MobileBy as By

from pages.base_page import BasePage

class LoginPage(BasePage):
    '''登录页面相关属性'''
    pwd_flash_msg = '手机号或密码错误'

    mobile_input_elem_locator = (By.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.xxzb.fenwoo:id/et_phone')")
    next_elem_button_locator = (By.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.xxzb.fenwoo:id/btn_next_step')")
    pwd_input_elem_locator = (By.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.xxzb.fenwoo:id/et_pwd')")
    submit_button_locator = (By.ANDROID_UIAUTOMATOR, "new UiSelector().text('确定')")
    error_info_locator = (By.ID, "com.xxzb.fenwoo:id/tv_message")
    invalid_info_locator = (By.CLASS_NAME, "layui-layer-content")

    @property
    def mobile_input_elem(self):
        return self.wait_presence_element(self.mobile_input_elem_locator)

    @property
    def pwd_input_elm(self):
        return self.wait_presence_element(self.pwd_input_elem_locator)

    @property
    def phone_error_msg_elem(self):
        '''错误提示信息'''
        return self.wait_visible_element(self.error_info_locator)

    @property
    def invalid_info_elem(self):
        '''手机或密码错误的元素'''
        return self.wait_visible_element(self.invalid_info_locator)

    @property
    def next_step_elem(self):
        return self.wait_click_element(self.next_elem_button_locator)

    def submit_phone(self, mobile):
        self.mobile_input_elem.send_keys(mobile)
        self.next_step_elem.click()

    def submit_pwd(self, pwd):
        self.pwd_input_elm.send_keys(pwd)
        self.wait_click_element(self.submit_button_locator).click()




