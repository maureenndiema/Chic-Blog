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
        self.user_Moh = User(username='maureen',password='1234', email='mandi@gmail.com')
        self.blog_Moh = Blog(title='love', blog='This is the ghetto', user=self.user_Moh)
        self.downvote_moh = Downvote(downvote='8', blog=self.blog_moh)

    def tearDown(self):
        Downvote.query.delete()
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.downvote_moh, Downvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.downvote_moh.downvote, '8')
        self.assertEquals(self.downvote_moh.blog, self.blog_moh)

    def test_save_upvote(self):
        self.downvote_moh.save_downvote()
        self.assertTrue(len(Downvote.query.all()) > 0)