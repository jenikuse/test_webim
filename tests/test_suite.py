import unittest

open_chat = unittest.TestLoader().loadTestsFromTestCase()
send_msg = unittest.TestLoader().loadTestsFromTestCase()
send_file = unittest.TestLoader().loadTestsFromTestCase()
rate_operator = unittest.TestLoader().loadTestsFromTestCase()
close_chat = unittest.TestLoader().loadTestsFromTestCase()


full_suite = [open_chat, send_msg, send_file, rate_operator, close_chat]

test_suite = unittest.TestSuite()


unittest.TextTestRunner(verbosity=2).run(test_suite)