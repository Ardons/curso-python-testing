import unittest
from faker import Faker

class UserTests(unittest.TestCase):
    
    def setUp(self):
        self.faker = Faker()