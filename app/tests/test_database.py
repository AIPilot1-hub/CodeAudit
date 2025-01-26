import unittest
from modules import database

class TestDatabase(unittest.TestCase):
    def test_query_user(self):
        result = database.query_user("testuser")
        self.assertIsNotNone(result)

    def test_insert_user(self):
        self.assertTrue(database.insert_user("newuser", "newpassword"))

if __name__ == "__main__":
    unittest.main()
