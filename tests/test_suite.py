import unittest

from test_open_chat import TestOpenChat
from test_connect_as_operator import TestConnectAsOperator
from test_send_message import TestSendMsg
from test_send_file import TestSendFile
from test_rate_operator import TestRateOperator
from test_close_chat import TestCloseChat


open_chat = unittest.TestLoader().loadTestsFromTestCase(TestOpenChat)
send_msg = unittest.TestLoader().loadTestsFromTestCase(TestSendMsg)

# FIXME send_file = unittest.TestLoader().loadTestsFromTestCase(TestSendFile)

connect_as_operator = unittest.TestLoader().loadTestsFromTestCase(TestConnectAsOperator)
rate_operator = unittest.TestLoader().loadTestsFromTestCase(TestRateOperator)

close_chat = unittest.TestLoader().loadTestsFromTestCase(TestCloseChat)


test_suite = unittest.TestSuite([open_chat, send_msg, connect_as_operator, rate_operator, close_chat])

unittest.TextTestRunner(verbosity=2).run(test_suite)
