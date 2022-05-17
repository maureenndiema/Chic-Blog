import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_user = User(username='maureen', password='1234')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('1234'))
