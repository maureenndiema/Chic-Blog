import unittest
from app.models import Blog, Downvote, User
from app import db

class DownvoteModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Moh = User(username='Mandi',password='1234', email='mandi@gmail.com')
        self.blog_Moh = Blog(title='love', blog='This is the ghetto', user=self.user_Moh)
        self.downvote_moh = Downvote(downvote='8', blog=self.blog_moh)