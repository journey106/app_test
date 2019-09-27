import pytest
from appium.webdriver import Remote

@pytest.fixture()
def init_app():
    caps = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "automationName": "uiautomator2",
        "deviceName": "Android Emulator",
        "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
        "appPackage": "com.xxzb.fenwoo",
        "noReset": False
    }
    driver = Remote(desired_capabilities=caps)
    print('app启动')
    yield driver
    driver.quit()


