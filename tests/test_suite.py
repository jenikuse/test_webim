import unittest

from test_open_chat import TestOpenChat
from test_send_message import TestSendMsg
from test_send_file import TestSendFile
from test_rate_operator import TestRateOperator
from test_close_chat import TestCloseChat


open_chat = unittest.TestLoader().loadTestsFromTestCase(TestOpenChat)
send_msg = unittest.TestLoader().loadTestsFromTestCase(TestSendMsg)
# send_file = unittest.TestLoader().loadTestsFromTestCase(TestSendFile)
# rate_operator = unittest.TestLoader().loadTestsFromTestCase(TestRateOperator)
close_chat = unittest.TestLoader().loadTestsFromTestCase(TestCloseChat)


# test_suite = [open_chat, send_msg, send_file, rate_operator, close_chat]
test_suite = unittest.TestSuite([open_chat, send_msg])


unittest.TextTestRunner(verbosity=2).run(test_suite)
