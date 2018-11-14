import unittest
import os
import time

from test_open_chat import driver
from selenium.webdriver.common.by import By


class TestSendFile(unittest.TestCase):
    def setUp(self):
        self.file_dir = "/Users/macbook/Downloads/f/"
        driver.find_element_by_css_selector(
            "button.webim-action:nth-child(1)").click()  # "three-dots" button

        # FIXME: can't load file to the server
        self.load_btn = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/ul/li[2]/label/span[2]")
    
    def test_07_send_file_valid(self):
        self.load_btn.send_keys(self.file_dir + "cat.jpg")
        time.sleep(2)
        last_msg = driver.find_element_by_css_selector(
            "li.webim-message:nth-child(6) > div:nth-child(3) > span:nth-child(1)")
        self.assertIn("Отправил", last_msg.text, "file with valid format was not loaded")

    def test_08_send_file_not_valid(self):
        self.load_btn.send_keys(self.file_dir + "cat.log")
        error = driver.find_element_by_css_selector(".webim-file-upload-error")
        self.assertIn(
            "Разрешены следующие типы: png, jpg, jpeg, doc, rtf, gif, txt, pdf, docx, webp.", 
            error.text, "no error after loading file with invalid extension")

    def test_09_send_file_large(self):
        self.load_btn.send_keys(self.file_dir + "tennis.pdf")
        error = driver.find_element_by_css_selector(".webim-file-upload-error")
        self.assertIn("Файл слишком большой для передачи.", error.text, 
                        "no error after loading file with large size")


if __name__ == "__main__":
    unittest.main()
