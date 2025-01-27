import unittest
from modules import user

class TestUser(unittest.TestCase):
    def test_create_user(self):
        self.assertTrue(user.create_user("testuser", "password"))

    def test_delete_user(self):
        self.assertTrue(user.delete_user("testuser"))

if __name__ == "__main__":
    unittest.main()
