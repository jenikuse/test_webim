import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait



url = 'https://demo-pro.webim.ru'
driver = webdriver.Firefox()
wait = Wait(driver, 30)


class TestOpenChat(unittest.TestCase):

    def test_01_open_webpage(self):
        driver.get(url)
        time.sleep(2)  # waiting for chat panel loading


    def test_02_open_chat(self):
        chat_panel = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div/a[2]/img")
        chat_panel.click()


    def test_03_check(self):

        msg_welcome = driver.find_element_by_css_selector(
            "li.webim-message:nth-child(1) > div:nth-child(3) > span:nth-child(1)").text

        self.assertIn("добро пожаловать", msg_welcome.lower())


    def test_10_close_driver(self):

        driver.close()


if __name__ == '__main__':
    unittest.main()

