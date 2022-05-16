import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_user = User(username='sani', password='12345')
