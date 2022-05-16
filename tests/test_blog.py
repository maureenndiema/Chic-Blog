import unittest
from app.models import Blog, User
from app import db

class BlogModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Moh = User(username='Mandi',password='1234', email='mandi@gmail.com')
        self.blog = Blog(title='Monday', blog='This is the ghetto', user=self.user_Moh)