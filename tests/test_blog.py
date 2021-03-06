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
        self.user_Moh = User(username='maureen',password='1234', email='mandi@gmail.com')
        self.blog = Blog(title='Fashion', blog='Life is too short to wear boring clothes!', user=self.user_Moh)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.blog, Blog))

    def test_check_instance_variables(self):
        self.assertEquals(self.blog.title, 'Fashion')
        self.assertEquals(self.blog.blog, 'Life is too short to wear boring clothes!')
        self.assertEquals(self.blog.user, self.user_Moh)

    def test_save_blog(self):
        self.blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)