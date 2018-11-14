import unittest
from random import choice
import time

from selenium.webdriver.common.keys import Keys
from test_open_chat import driver


class TestSendMsg(unittest.TestCase):

    def setUp(self):
        self.text_area = driver.find_element_by_css_selector(".webim-message-area")
        self.assertTrue(self.text_area.is_displayed(),
                        "field for message input is not displaying")
        
        self.msg_templates_positive = {
            "i love chatting myself;",
            "Eat @ sleep @ testing",
            ",.%#+=!@^*()",
            "∆",
            "&",  # BUG: ampersand (&) --> '&amp;'
            20 * "many-" + "elephants-live-in-my-head, doctor!",
            50 * "WЁ are зе чемпiонs? Май френд. ",
            "https://goo.gl/3smbEA",
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

    def test_06_send_messages_positive(self):
        text_area = self.text_area

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
                # FIXME: [BUG] ampersand (&) transforms to the next string value: '&amp;'
                if msg_to_send == "&" and msg_to_send != displayed_msg:
                    print("symbol \'" + msg_to_send +
                          "\' transforms to the next combination: \'" + displayed_msg + "\'")
            text_area.clear()

    def test_07_send_messages_negative(self):
        text_area = self.text_area

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
    
    # TODO: add comparing for emoji (sent and in chat history)
    def test_08_send_emoji(self):
        text_area = self.text_area
        btn_emoji = driver.find_element_by_css_selector("button.webim-action:nth-child(3)")
        btn_emoji.click()
        time.sleep(3)  # for loading emoji panel. increase if low internet connection
        emoji_list = driver.find_elements_by_class_name("webim-emoji")

        for _ in range(5):
            emoji = choice(emoji_list)
            emoji.click()
            text_area.send_keys(Keys.ENTER)
            self.assertEqual("", text_area.text, "after sending emoji text field is not empty") 
            text_area.clear()

        btn_emoji.click()  # close emoji panel

    # FIXME negative case for rating should be before operator reply
    @unittest.skip
    def test_09_rate_operator_before_reply(self):
        time.sleep(2)
        # "three-dots" menu button
        driver.find_element_by_css_selector(
            "button.webim-action:nth-child(1)").click()
        driver.find_element_by_class_name("webim-chat-action-rate").click()

        rate_elements = driver.find_elements_by_class_name("webim-icon-operator-rate")
        random_rating = choice(rate_elements)
        random_rating.click()

        self.rate_btn = driver.find_element_by_css_selector(".webim-js-button-style")

        rate_error = driver.find_element_by_css_selector(".webim-rate-error")
        self.assertIn("Нет оператора для выставления оценки", rate_error.text,
                      "no message that operator is not selected")

        close_rate_btn = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/span")
        close_rate_btn.click()


if __name__ == "__main__":
    unittest.main()
