import unittest
from modules import auth

class TestAuth(unittest.TestCase):
    def test_authenticate_success(self):
        self.assertTrue(auth.authenticate("admin", "admin123"))

    def test_authenticate_failure(self):
        self.assertFalse(auth.authenticate("admin", "wrongpassword"))

if __name__ == "__main__":
    unittest.main()
