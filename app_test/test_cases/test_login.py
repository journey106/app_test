import time
import unittest

# from ddt import ddt, data
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.nav_page import NavPage

from datas.login_data import user_login_success, user_pwd_error, user_mobile_error


class TestLogin:

    @pytest.mark.login
    @pytest.mark.parametrize('user_data', user_mobile_error)
    def test_login_mobile_error(self, user_data, init_app):
        driver = init_app
        print('开始****')
        # 欢迎页面左划，点击进入首页
        # 首页，点击登录注册
        # 输入手机号码，点击下一步，密码
        # 断言
        HomePage(driver).welcome()
        NavPage(driver).user_elem.click()
        login_page = LoginPage(driver)
        login_page.submit_phone(user_data['mobile'])
        assert (user_data['msg'] == login_page.phone_error_msg_elem.text)

    @pytest.mark.login
    @pytest.mark.parametrize('user_data', user_pwd_error)
    def test_login_pwd_error(self, user_data, init_app):
        driver = init_app
        HomePage(driver).welcome()
        NavPage(driver).user_elem.click()
        login_page = LoginPage(driver)
        login_page.submit_phone(user_data['mobile'])
        # 获取密码
        login_page.submit_pwd(user_data['pwd'])
        assert (user_data['msg'] == login_page.toast(login_page.pwd_flash_msg).text)

    # @pytest.mark.login
    # @pytest.mark.parametrize('user_data', user_login_success)
    # def test_login_success(self, user_data, init_app):
    #     driver = init_app
    #     HomePage(driver).welcome()
    #     NavPage(driver).user_elem.click()
    #     login_page = LoginPage(driver)
    #     login_page.submit_phone(user_data['mobile'])
    #     # 获取密码
    #     login_page.submit_pwd(user_data['pwd'])
    #     time.sleep(2)
    #     print(driver.current_activity)
    #     assert (user_data['msg'] == login_page.toast(login_page.pwd_flash_msg).text)

if __name__ == '__main__':
    unittest.main()