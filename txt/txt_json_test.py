import unittest

from txt_json import changeConfig


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        testIn = {"test1": {"value": "Hello, World1!"},
                  "test2": {"value": "Hello, World2!"}}
        testOut = {"test1": {"value": "Bonjour le monde"},
                   "test2": {"value": "Hello, World2!"}}
        result = changeConfig(testIn)
        self.assertEqual(result, testOut)


if __name__ == '__main__':
    unittest.main()
