import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from test_open_chat import load_data


class TestConnectAsOperator(unittest.TestCase):


    def setUp(self):
        self.link_operator = "http://demo.webim.ru/webim/"
        self.operator = {
            "email": "o@webim.ru",
            "pw": "password"
        }
        self.driver = webdriver.Firefox()
        self.driver.get(self.link_operator)

        # fill login fields
        self.driver.find_element_by_id("login_or_email").send_keys(self.operator["email"])
        self.driver.find_element_by_id("password").send_keys(self.operator["pw"])
        self.driver.find_element_by_id("is_remember").click()
        self.driver.find_element_by_css_selector("button.btn-primary").click()
        self.driver.find_element_by_css_selector(
            ".nav > li:nth-child(1) > a:nth-child(1)").click()  # go to the operator panel 

    def test_06_operator_replies(self):
        time.sleep(2)  # while page with clients will be updated
        user_name = load_data["name"]
        chats = self.driver.find_elements_by_class_name("visitor-name")  # SE objects of different chats

        for chat_name in chats:
            if chat_name.text == user_name:
                chat_name.click()  # go to the chat with our user
                time.sleep(1.5)  # wait while loading chat

        self.driver.find_element_by_css_selector(".chat_message_textarea").send_keys("молодец")
        self.driver.find_element_by_css_selector(".chat_message_textarea").send_keys(Keys.ENTER)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main()
