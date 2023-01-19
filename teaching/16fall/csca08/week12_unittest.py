import unittest
from my_file import *

class TestRemoveDupValue(unittest.TestCase):
    def test_empty_dict(self):
        d = {}
        actual = remove_dup_values(d)
        expected = 0
        d_after = {}
        self.assertEqual(
            actual,
            expected,
            'testing with an empty dict'
        )
        self.assertEqual(
            d,
            d_after,
            'testing mutation with an empty dict'
        )

    def test_dict_many_ele_one_dup(self):
        d = {0: 1, 1: 1, 2: 2}
        actual = remove_dup_values(d)
        expected = 2
        d_after = {2: 2}
        self.assertEqual(
            actual,
            expected,
            'testing with an empty dict'
        )
        self.assertEqual(
            d,
            d_after,
            'testing mutation with an empty dict'
        )

if __name__ == '__main__':
    unittest.main(exit=False)
