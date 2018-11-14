import unittest

import time

from test_open_chat import driver


class TestSendFile(unittest.TestCase):
    def setUp(self):
        self.file_dir = "your/path/to/file"
        self.files_name = {
            "valid": [
                "cat.jpg",
                "cat.png",
                "cat.jpeg",
                "cat.gif",
                "file.doc",
                "file.rtf",
                "file.txt",
                "file.pdf",
                "file.docx",
                "file.wepb"
            ],
            "not_valid": [
                "cat.jpg.zip",
                "cat.mp3",
                "cat.NaN",
                "file.log",
            ]
        }

        driver.find_element_by_css_selector(
            "button.webim-action:nth-child(1)").click()  # "three-dots" button

        # FIXME: can't load file to the server
        self.load_btn = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/ul/li[2]/label/span[2]")
    
    def test_10_send_file_valid(self):
        for file_name in self.files_name["valid"]:
            self.load_btn.send_keys(self.file_dir + file_name)
            time.sleep(1)

            last_msg = driver.find_element_by_css_selector(
                "li.webim-message:nth-child(6) > div:nth-child(3) > span:nth-child(1)")
            self.assertIn("Отправил", last_msg.text,
                          "file \'" + file_name + "\' with valid format was not uploaded")

    def test_11_send_file_not_valid(self):
        for file_name in self.files_name["not_valid"]:
            self.load_btn.send_keys(self.file_dir + file_name)
            error = driver.find_element_by_css_selector(".webim-file-upload-error")
            self.assertIn("Разрешены следующие типы: png, jpg, jpeg, doc, rtf, gif, txt, pdf, docx, webp.",
                          error.text, "no error after loading \'" + file_name + "\' file with invalid extension")

    def test_12_send_file_large(self):
        self.load_btn.send_keys(self.file_dir + "book.pdf")
        error = driver.find_element_by_css_selector(".webim-file-upload-error")

        self.assertIn("Файл слишком большой для передачи.", error.text,
                      "no error after loading file with large size")


if __name__ == "__main__":
    unittest.main()
