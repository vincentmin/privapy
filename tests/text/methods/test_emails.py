import unittest
from privapy.text.methods import EmailCleaner


class TestEmailCleaner(unittest.TestCase):
    def setUp(self):
        self.email_cleaner = EmailCleaner()

    def test_clean_email(self):
        text = "Please contact me at john.doe@example.com"
        expected_output = "Please contact me at <<EMAIL>>"
        self.assertEqual(self.email_cleaner(text), expected_output)

    def test_clean_email_with_custom_replacement(self):
        text = "Please contact me at john.doe@example.com"
        expected_output = "Please contact me at [email]"
        email_cleaner = EmailCleaner("[email]")
        self.assertEqual(email_cleaner(text), expected_output)


if __name__ == "__main__":
    unittest.main()
