import unittest

from selenium import webdriver


driver = webdriver.Firefox()


class TestOpenChat(unittest.TestCase):

    def test_01_close_chat(self):
        btn_close = driver.find_element_by_css_selector("div.webim-action-close")
        btn_close.click()

    def test_02_check_if_chat_closed(self):
        msg_area = driver.find_element_by_css_selector(".webim-message-area")
        self.assertFalse(msg_area.is_displayed())

    def test_10(self):
        driver.close()


if __name__ == '__main__':
    unittest.main()
