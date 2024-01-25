#!/usr/bin/env python3
""" unit test for utils.access_nested_map
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1},("a",), a, 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, path=("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        self.assertRaises(access_nested_map(nested_map, path), expected)

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.get_json')
    def test_get_json(self, test_url, test_payload):
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        result = get_json(test_url)

        mock_get_json.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()
    
    def test_memoize(self):
        test_instance = self.TestClass()

        with patch.object(test_instance, 'a_method') as mock_a_method:
            result_1 = test_instance.a_property
            result_2 = test_instance.a_property

            mock_a_method.assert_called_once()

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)

if __name__ == "__main__":
    unittest.main()
