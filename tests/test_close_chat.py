import unittest

from test_open_chat import driver


class TestCloseChat(unittest.TestCase):

    def test_15_close_chat(self):
        btn_close = driver.find_element_by_css_selector("div.webim-action-close")
        self.assertTrue(btn_close.is_displayed(),
                        "chat close button is not displaying")
        btn_close.click()
        self.assertFalse(btn_close.is_displayed(), 
        "chat close button is displaying, but chat window has been closed")

    def test_16_reopen_chat(self):
        driver.find_element_by_css_selector(
            ".webim_button > img:nth-child(1)").click()
        msg_area = driver.find_element_by_css_selector(".webim-dialogues")
        self.assertTrue(msg_area.is_displayed(), "chat is not displaying")

    def test_17_minimize_chat(self):
        btn_minimize = driver.find_element_by_css_selector(".webim-action-minimize")
        self.assertTrue(btn_minimize.is_displayed(),
                        "chat minimize button is not displaying")
        btn_minimize.click()
        self.assertFalse(btn_minimize.is_displayed(), "chat minimize button is \
                        displaying, but chat window has been minimized")

        driver.close()

if __name__ == "__main__":
    unittest.main()
