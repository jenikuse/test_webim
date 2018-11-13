import unittest
from random import choice
import time
from selenium.webdriver.common.keys import Keys

from test_open_chat import driver


class TestSendMsg(unittest.TestCase):

    def setUp(self):
        self.msg_templates_positive = {
            "i love chatting alone;",
            "Eat @ sleep @ testing",
            ",.%#+=!@^*()",
            "∆",
            20 * "many-" + "elephants-live-in-my-head, doctor",
            30 * "WЁ are зе чемпiонs? Май френд."
        }
        self.msg_templates_negative = [
            " ",
            20 * " ",
            1000 * " ",
            "\t\t\n \n\t "
        ]
        self.operator_msg = [
            "Добро пожаловать в демо приложение для демонстрации чата.",
            "Пожалуйста, подождите немного, к Вам присоединится оператор...",
            "К сожалению, оператор сейчас не может ответить."
        ]

    def test_04_send_messages_positive(self):
        text_area = driver.find_element_by_css_selector(".webim-message-area")
        self.assertTrue(text_area.is_displayed(),
                        "field for message input is not displaying")

        for msg_to_send in self.msg_templates_positive:
            text_area.send_keys(msg_to_send)
            text_area.send_keys(Keys.ENTER)

            displayed_messages = driver.find_elements_by_class_name(
                "webim-message-body")
            displayed_msg = displayed_messages.pop().text
            while displayed_msg in self.operator_msg:
                displayed_msg = displayed_messages.pop().text

            self.assertEqual(msg_to_send, displayed_msg,
                             "sent and displayed messages are different")

    def test_05_send_messages_negative(self):
        pass

    def test_03_send_emoji(self):
        btn_emoji = driver.find_element_by_css_selector("button.webim-action:nth-child(3)")
        btn_emoji.click()
        time.sleep(2)  # for loading emojis panel

        emoji_list = driver.find_elements_by_css_selector("span.webim-emoji:nth-child(57)")
        emoji = choice(emoji_list)  # choice random emoji


if __name__ == "__main__":
    unittest.main()
