import unittest
from services import email_service, data_processor

class TestServices(unittest.TestCase):
    def test_send_email(self):
        self.assertTrue(email_service.send_email("user@example.com", "Test", "This is a test email."))

    def test_process_data(self):
        processed = data_processor.process_data("Sample Data")
        self.assertEqual(processed, "sample_data")

if __name__ == "__main__":
    unittest.main()
