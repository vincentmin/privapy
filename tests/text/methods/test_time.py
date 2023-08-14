import unittest
from privapy.text.methods.regex import TimeCleaner


class TestTimeCleaner(unittest.TestCase):
    def setUp(self):
        self.time_cleaner = TimeCleaner()

    def test_clean_time(self):
        text = "The meeting will start at 10:30 AM"
        expected_output = "The meeting will start at <<TIME>> AM"
        self.assertEqual(self.time_cleaner(text), expected_output)

    def test_clean_time_with_custom_replacement(self):
        text = "The meeting will start at 10:30 AM"
        expected_output = "The meeting will start at [time] AM"
        time_cleaner = TimeCleaner("[time]")
        self.assertEqual(time_cleaner(text), expected_output)


if __name__ == "__main__":
    unittest.main()
