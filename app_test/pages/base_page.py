from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

from common.key_code import KeyCode
from handle_log import do_logger
import config
import os
from datetime import datetime
from appium.webdriver import Remote


class BasePage:

    def __init__(self, driver: Remote):
        self.driver = driver
        self.driver.maximize_window()

    def wait_click_element(self, locator, timeout=20, poll=0.5):
        try:
            return WebDriverWait(self.driver, timeout, poll).until(EC.element_to_be_clickable(locator))
        except (TimeoutException, NoSuchElementException) as e:
            do_logger.error('定位出错：{}'.format(e))
            # 保存错误截图
            self.save_screenshot()

    def wait_visible_element(self, locator, timeout=20, poll=0.5):
        try:
            return WebDriverWait(self.driver, timeout, poll).until(EC.visibility_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            do_logger.error("定位出错: {}".format(e))
            # 保存错误截图
            self.save_screenshot()

    def wait_presence_element(self, locator, timeout=20, poll=0.5):
        try:
            return WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located(locator))
        except (NoSuchElementException, TimeoutException) as e:
            do_logger.error('定位出错:{}'.format(e))
            # 保存错误截图
            self.save_screenshot()

    def wait_visible_elements(self, locator, timeout=20, poll=0.5):
        try:
            return WebDriverWait(self.driver, timeout, poll).until(EC.visibility_of_all_elements_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            do_logger.error("定位出错: {}".format(e))
            # 保存错误截图
            self.save_screenshot()

    def wait_presence_elements(self, locator, timeout=20, poll=0.5):
        try:
            return WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_all_elements_located(locator))
        except (NoSuchElementException, TimeoutException) as e:
            do_logger.error('定位出错:{}'.format(e))
            # 保存错误截图
            self.save_screenshot()

    def wait_presence_alert(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.alert_is_present())
        except (NoSuchElementException, TimeoutException) as e:
            do_logger.error('定位出错:{}'.format(e))
            # 保存错误截图
            self.save_screenshot()

    def find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            do_logger.error("定位出错：{}".format(e))
            self.save_screenshot()

    def generate_screen_file_name_by_ts(self):
        '''生成文件名'''
        local_time = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        return ''.join([local_time, '.png'])

    def save_screenshot(self):
        '''自动化保存截图'''
        pic_dir = config.LOG_IMG
        file_name = os.path.join(pic_dir, self.generate_screen_file_name_by_ts())
        return self.driver.save_screenshot(file_name)

    # def get_url(self):
    #     return self.driver.current_url
    #
    # # def switch_window(self, window_name):
    # #     windows = self.driver.window_handles
    # #     return self.driver.switch_to.window(windows[window_name])
    #
    # def switch_window_by_index(self, index):
    #     windows = self.driver.window_handles
    #     # return self.driver.switch_to.window(windows[-1])  # 切换到最新打开的窗口
    #     # return self.driver.switch_to.window(windows[0])   # 切换到第一个窗口
    #     # return self.driver.switch_to.current_window_handle   # 获取当前窗口句柄
    #     return self.driver.switch_to.window(windows[index])

    def switch_frame(self, locator=None, timeout=20, fqc=20):
        """切换iframe"""
        if not locator:
            return self.driver.switch_to.default_content()
        return WebDriverWait(self.driver, timeout, poll_frequency=fqc).until(
            EC.frame_to_be_available_and_switch_to_it(locator))

    # def switch_to_default_iframe(self):
    #     return self.driver.switch_to.default_content()
    #     # return wait.until(EC.alert_is_present()).accept()

    # @property
    # def switch_alert(self):
    #     self.wait_presence_alert()
    #     return self.driver.switch_to.alert

    # 鼠标操作
    # 滚动窗口
    # 键盘操作
    # def double_click(self, elem):
    #     '''双击'''
    #     action_chains = ActionChains(self.driver)
    #     action_chains.double_click(elem).perform()
    #
    # def context_click(self, elem):
    #     '''右击'''
    #     action_chains = ActionChains(self.driver)
    #     action_chains.context_click(elem).perform()
    #
    # def drag_and_drop(self, elem, target):
    #     '''拖放操作'''
    #     action_chains = ActionChains(self.driver)
    #     action_chains.drag_and_drop(elem, target).perform()
    #
    # def keyboard(self, elem, key, *args):
    #     '''键盘操作'''
    #     # action_chains = ActionChains(self.driver)
    #     # action_chains.key_down(key)
    #     return elem.send_keys(key, *args)


    def scroll_window(self, width, height):
        '''滚动窗口'''
        return self.driver.execute_script("window.scrollTo({}, {})".format(width, height))

    def select_by_index(self, elem, index):
        '''下拉框操作'''
        return Select(elem).select_by_index(index)

    def select_by_value(self, elem, value):
        return Select(elem).select_by_value(value)

    def select_by_name(self, elem, value):
        return Select(elem).select_by_visible_text(value)

    def switch_context(self, context_name=None):
        '''上下文切换 WEBVIEW,NATIVE_APP  混合应用 h5'''
        if context_name is None:
            return self.driver.switch_to.context("NATIVE_APP")
        cur_contexts = self.driver.contexts
        for context in cur_contexts:
            if context == context_name:
                self.driver.switch_to.context(context_name)

    @property
    def size(self):
        return self.driver.get_window_size()

    @property
    def width(self):
        return self.size['width']

    @property
    def height(self):
        return self.size['height']

    def swipe_left(self, duration=200):
        '''左划'''
        self.driver.swipe(self.width*0.9, self.height*0.5, self.width*0.1, self.height*0.5, duration)

    def swipe_right(self, duration=200):
        '''右划'''
        self.driver.swipe(self.width*0.1, self.height*0.5, self.width*0.9, self.height*0.5, duration)

    def swipe_down(self, duration=200):
        '''下划'''
        self.driver.swipe(self.width*0.5, self.height*0.1, self.width*0.5, self.height*0.9, duration)

    def swipe(self, direction):
        if direction == 'left':
            return self.swipe_left()
        elif direction == 'right':
            return self.swipe_right()
        elif direction == 'down':
            return self.swipe_down()

    def jiugongge(self, e, points, duration=200):
        '''九宫格解锁'''
        # [1, 3, 4, 6, 9]
        action = TouchAction(self.driver)

        start_x = e.rect['x']
        start_y = e.rect['y']
        width = e.rect['width']
        height = e.rect['height']

        static_points = [
            {"x": start_x + width * 1 / 6, "y": start_y + height * 1 / 6},
            {"x": start_x + width * 3 / 6, "y": start_y + height * 1 / 6},
            {"x": start_x + width * 5 / 6, "y": start_y + height * 1 / 6},
            {"x": start_x + width * 1 / 6, "y": start_y + height * 3 / 6},
            {"x": start_x + width * 3 / 6, "y": start_y + height * 3 / 6},
            {"x": start_x + width * 5 / 6, "y": start_y + height * 3 / 6},
            {"x": start_x + width * 1 / 6, "y": start_y + height * 5 / 6},
            {"x": start_x + width * 3 / 6, "y": start_y + height * 5 / 6},
            {"x": start_x + width * 5 / 6, "y": start_y + height * 5 / 6},
        ]
        action.press(**static_points[points[0]-1]).wait(duration)
        for point in points[1:]:
            action.move_to(**static_points[point - 1]).wait(duration)
        action.release().perform()

    def send_keycode(self, key):
        '''发送物理按键'''
        return self.driver.press_keycode(key)

    def volumn_up(self):
        '''音量增'''
        return self.send_keycode(KeyCode.VOLUME_UP)

    def volumn_down(self):
        '''音量减'''
        return self.send_keycode(KeyCode.VOLUME_DOWN)

    def confirm(self):
        '''回车'''
        return self.send_keycode(KeyCode.ENTER)

    def toast(self, toast_text):
        self.wait_presence_element((MobileBy.XPATH, f"//*[contains(@text, {toast_text})]"), timeout=20 ,poll=0.1)

    def click(self, locator):
        return self.wait_click_element(locator).click()

    def press(self, x, y):
        action = TouchAction(self.driver)
        return action.press(x, y).perform()

    def move_to(self, x, y):
        action = TouchAction(self.driver)
        return action.move_to(x, y).perform()





