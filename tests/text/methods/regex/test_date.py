import unittest
from privapy.text.methods.regex import DateCleaner


class TestDateCleaner(unittest.TestCase):
    def setUp(self):
        self.date_cleaner = DateCleaner()

    def test_clean_date(self):
        text = "The event will take place on 2022-01-01"
        expected_output = "The event will take place on <<DATE>>"
        self.assertEqual(self.date_cleaner(text), expected_output)

    def test_clean_date_with_custom_replacement(self):
        text = "The event will take place on 01/01/2022"
        expected_output = "The event will take place on [date]"
        date_cleaner = DateCleaner("[date]")
        self.assertEqual(date_cleaner(text), expected_output)


if __name__ == "__main__":
    unittest.main()
