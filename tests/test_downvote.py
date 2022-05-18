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
        self.blog_Moh = Blog(title='Fashion', blog='Life is too short to wear boring clothes!', user=self.user_Moh)
        self.downvote_Moh = Downvote(downvote='8', blog=self.blog_Moh)

    def tearDown(self):
        Downvote.query.delete()
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.downvote_Moh, Downvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.downvote_Moh.downvote, '8')
        self.assertEquals(self.downvote_Moh.blog, self.blog_Moh)

    def test_save_upvote(self):
        self.downvote_Moh.save_downvote()
        self.assertTrue(len(Downvote.query.all()) > 0)