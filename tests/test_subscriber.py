import unittest
from app.models import Subscriber
from app import db

class SubscriberModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Comment class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.subscriber = Subscriber(email='mandi@gmail.com')

    def tearDown(self):
        Subscriber.query.delete()
