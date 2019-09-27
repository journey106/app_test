import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    '''首页'''
    # 引导页页数
    welcome_pages = 3

    welcome_enter_button_locator = (By.ID, "com.xxzb.fenwoo:id/btn_start")

    def welcome(self):
        '''滑屏，点击欢迎页进入首页'''
        time.sleep(2)
        print('''首页''')
        for i in range(self.welcome_pages):
            print('滑屏开始')
            self.swipe_left()
            time.sleep(0.2)
        self.wait_click_element(self.welcome_enter_button_locator).click()
        