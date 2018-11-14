import unittest
import time

from selenium import webdriver

from testing_utils import generate_name

driver = webdriver.Firefox()
url = "https://demo-pro.webim.ru"


load_data = {
            "name": generate_name(),
            "phone": "9991112233",
            "email": "mail@mail.ru",
            "code_phrase": "111"
        }  # for user edit profile 


class TestOpenChat(unittest.TestCase):
        
    def test_01_open_webpage(self):
        driver.get(url)
        self.assertIn("веб мессенджер", driver.title.lower())
        time.sleep(3)  # waiting for chat panel loading

    def test_02_open_chat(self):
        chat_panel = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div/div/a[2]/img")
        self.assertTrue(chat_panel.is_displayed())
        chat_panel.click()

    def test_03_check_that_chat_is_open(self):
        msg_welcome = driver.find_element_by_css_selector(
            "li.webim-message:nth-child(1) > div:nth-child(3) > span:nth-child(1)").text
        self.assertIn("добро пожаловать", msg_welcome.lower())

    def test_04_edit_profile(self):
        driver.find_element_by_css_selector(
            "button.webim-action:nth-child(1)").click()  # three-dots menu
        
        edit_data_btn = driver.find_element_by_css_selector(
            "li.webim-chat-action:nth-child(5) > span:nth-child(1) > span:nth-child(2)")
        edit_data_btn.click()

        name = driver.find_element_by_css_selector(
            ".webim-contact > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")
        name.send_keys(load_data["name"])
        
        phone = driver.find_element_by_css_selector(
            ".webim-contact > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > input:nth-child(2)")
        phone.send_keys(load_data["phone"])
        
        email = driver.find_element_by_css_selector(
            ".webim-contact > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > input:nth-child(2)")
        email.send_keys(load_data["email"])

        code_phrase = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]/div[2]/div/div[1]/div[8]/label/input")
        code_phrase.send_keys(load_data["code_phrase"])

        processing_data = driver.find_element_by_css_selector(
            "div.webim-processing-personal-data-block:nth-child(2) > input:nth-child(1)")
        processing_data.click()

        submit_btn = driver.find_element_by_css_selector(
            "button.processing-personal-data-dependence:nth-child(1)")
        submit_btn.click()

    def test_05_is_profile_edited(self):
        last_msg = driver.find_element_by_css_selector(
            "li.webim-message:nth-child(3) > div:nth-child(3) > span:nth-child(1)")
        self.assertIn("Вы указали контактные данные.", last_msg.text, "data not edited")

        for key, value in load_data.items():
            if key == "phone":
                continue
            self.assertIn(load_data[key], last_msg.text, key + " has not been edited")


if __name__ == "__main__":
    unittest.main()

