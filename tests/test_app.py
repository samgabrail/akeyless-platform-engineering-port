import unittest

class TestSimple(unittest.TestCase):
    def test_true_is_true(self):
        """A trivial test that will always pass"""
        self.assertTrue(True)

    def test_one_plus_one(self):
        """Basic math test"""
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
