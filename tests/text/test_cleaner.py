import unittest
from privapy.text import TextCleaner
from privapy.text.methods.regex import EmailCleaner, DateCleaner


class TestTextCleaner(unittest.TestCase):
    def setUp(self):
        self.text_cleaner = TextCleaner("regex")

    def test_clean_text(self):
        text = "Please contact me at john.doe@example.com on 2022-01-01 at 10:30 AM"
        expected_output = "Please contact me at <<EMAIL>> on <<DATE>> at <<TIME>> AM"
        self.assertEqual(self.text_cleaner.clean(text), expected_output)

    def test_clean_text_with_custom_steps(self):
        text = "Please contact me at john.doe@example.com on 2022-01-01 at 10:30 AM"
        expected_output = "Please contact me at [email] on [date] at 10:30 AM"
        steps = [EmailCleaner("[email]"), DateCleaner("[date]")]
        text_cleaner = TextCleaner(steps)
        self.assertEqual(text_cleaner.clean(text), expected_output)


if __name__ == "__main__":
    unittest.main()
