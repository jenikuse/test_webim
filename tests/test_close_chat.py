import unittest

from test_open_chat import driver


class TestCloseChat(unittest.TestCase):

    def test_15_close_chat(self):
        btn_close = driver.find_element_by_css_selector("div.webim-action-close")
        self.assertTrue(btn_close.is_displayed(),
                        "chat close button is not displaying")
        btn_close.click()

    def test_16_check_if_chat_closed(self):
        msg_area = driver.find_element_by_css_selector(".webim-dialogues")
        self.assertFalse(msg_area.is_displayed(),
                         "chat was not closed")
        driver.close()


if __name__ == "__main__":
    unittest.main()
