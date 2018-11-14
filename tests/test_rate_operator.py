import unittest
from random import choice
import time

from selenium.common.exceptions import NoSuchElementException

from test_open_chat import driver


class TestRateOperator(unittest.TestCase):

    def test_13_rate_after_operator_responds(self):
        time.sleep(5)
        # "three-dots" menu button
        driver.find_element_by_css_selector(
            "button.webim-action:nth-child(1)").click()
        driver.find_element_by_class_name("webim-chat-action-rate").click()

        rate_elements = driver.find_elements_by_class_name("webim-icon-operator-rate")
        random_rating = choice(rate_elements)
        random_rating.click()

        self.rate_btn = driver.find_element_by_css_selector(".webim-js-button-style")

        self.assertTrue(self.rate_btn.is_displayed(), 
                        "the rating should be put after the answer of the operator")
        self.rate_btn.click()
        success_icon = driver.find_element_by_css_selector("div.webim-icon")
        self.assertTrue(success_icon,
                        "a green check mark does not appears after rating.")
        try:
            rate_error = driver.find_element_by_css_selector(".webim-rate-error")
        except NoSuchElementException:
            pass  # normal, because we are checking that no one rare error in chat window
        else:
            self.assertNotIn("Нет оператора для выставления оценки", rate_error.text,
                             "should not been message that operator is not selected")

if __name__ == "__main__":
    unittest.main()
