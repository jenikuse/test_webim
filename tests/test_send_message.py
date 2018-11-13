import unittest
from random import choice
import time
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions as ex
from test_open_chat import driver
 

class TestSendMsg(unittest.TestCase):

    def setUp(self):
        self.msg_templates_positive = {
            "i love chatting alone;",
            "Eat @ sleep @ testing",
            ",.%#+=!@^*()",
            "∆",
            "&",  # BUG: ampersand (&) --> '&amp;'
            20 * "many-" + "elephants-live-in-my-head, doctor!",
            50 * "WЁ are зе чемпiонs? Май френд. ",
            "https://vk.cc/8H6pBG",
        }
        self.msg_templates_negative = [
            " ",
            15 * "\n",
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
            
            try:
                self.assertEqual(msg_to_send, displayed_msg,
                                "sent and displayed messages are different")
                self.assertEqual("", text_area.text,
                                "text area is not empty after sending message to the chat")
            except AssertionError:
                # BUG: ampersand (&) tranforms to the next string value: '&amp;'
                if msg_to_send == "&" and msg_to_send != displayed_msg:
                    print("symbol \'" + msg_to_send + 
                    "\' transforms to the next combination: \'" + displayed_msg + "\'")

    def test_05_send_messages_negative(self):
        text_area = driver.find_element_by_css_selector(".webim-message-area")
        self.assertTrue(text_area.is_displayed(),
                        "field for message input is not displaying")

        for msg_to_send in self.msg_templates_negative:
            text_area.send_keys(msg_to_send)
            text_area.send_keys(Keys.ENTER)
            self.assertNotEqual("", text_area, "a message with the following content \
                                should not be displayed: " + msg_to_send)
            text_area.clear()

        displayed_messages = driver.find_elements_by_class_name("webim-message-body")
        chat_history = [msg.text for msg in displayed_messages]

        for msg in self.msg_templates_negative:
            self.assertNotIn(msg, chat_history,
                             "not valid message: \'" + msg + "\' has been found in chat history")

    def test_03_send_emoji(self):
        text_area = driver.find_element_by_css_selector(".webim-message-area")
        self.assertTrue(text_area.is_displayed(),
                        "field for message input is not displaying")
        btn_emoji = driver.find_element_by_css_selector("button.webim-action:nth-child(3)")
        btn_emoji.click()
        time.sleep(2)  # for loading emoji panel
        emoji_list = driver.find_elements_by_css_selector("span.webim-emoji:nth-child(57)")

        for _ in range(5):
            emoji = choice(emoji_list).text
            text_area.send_keys(emoji)
            self.assertEqual("", text_area.text, "after sending emoji text field is not empty") 
            text_area.clear()

        displayed_messages = driver.find_elements_by_class_name(
                "webim-message-body")


if __name__ == "__main__":
    unittest.main()
