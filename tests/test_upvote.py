import unittest
from app.models import Blog, Upvote, User
from app import db

class UpvoteModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Moh = User(username='mandi',password='1234', email='mandi@gmail.com')
        self.blog_moh = Blog(title='fashion', blog='Life is too short to wear boring clothes!', user=self.user_Moh)

        self.upvote_moh = Upvote(upvote='2', blog=self.blog_moh)

    def tearDown(self):
        Upvote.query.delete()
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.upvote_moh, Upvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.upvote_moh.upvote, '2')
        self.assertEquals(self.upvote_moh.blog, self.blog_moh)

    def test_save_upvote(self):
        self.upvote_moh.save_upvote()
        self.assertTrue(len(Upvote.query.all()) > 0)
