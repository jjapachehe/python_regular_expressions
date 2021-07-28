import unittest
import regex as rx

class Project_Test(unittest.TestCase):
    
    def test_regex(self):
        str = 'email:d_funk@example.org'
        expected = 'email:'
        actual = rx.regex_email(str)
        self.assertEquals(actual, expected)
        
    def test_nopfx(self):
        str = 'd_funk@example.org'
        expected = 'email:d_funk@example.org'
        actual = rx.regex_email(str)
        self.assertEquals(actual, expected)
    