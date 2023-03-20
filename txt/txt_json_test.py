import unittest

from txt_json import changeConfig


class TestTxtJson(unittest.TestCase):
    def test_txt_json_changeConfig_no_data(self):
        """
        Test changeConfig function: no data
        """
        testIn = None
        testOut = {}
        result = changeConfig(testIn)
        self.assertEqual(result, testOut)

    def test_txt_json_changeConfig_no_key_value(self):
        """
        Test changeConfig function: no test1 key value
        """
        testIn = {"test2": {"value": "Hello, World1!"},
                  "test3": {"value": "Hello, World2!"}}
        testOut = {"test2": {"value": "Hello, World1!"},
                   "test3": {"value": "Hello, World2!"}}
        result = changeConfig(testIn)
        self.assertEqual(result, testOut)

    def test_txt_json_changeConfig(self):
        """
        Test changeConfig function: OK
        """
        testIn = {"test1": {"value": "Hello, World1!"},
                  "test2": {"value": "Hello, World2!"}}
        testOut = {"test1": {"value": "Bonjour le monde"},
                   "test2": {"value": "Hello, World2!"}}
        result = changeConfig(testIn)
        self.assertEqual(result, testOut)


if __name__ == '__main__':
    unittest.main()
