import unittest
import app

class ClassTests(unittest.TestCase):
    def test_01(self):
        result = app.method()
        result.assertEqual('Hello World!', result)

