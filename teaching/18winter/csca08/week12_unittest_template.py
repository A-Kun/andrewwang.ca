import unittest # import the unit test module
import my_file # import the module we want to test

class TestFunctionName(unittest.TestCase): # have one test class for each function
    def test_case_name(self): # each test case must start with "test_"
        self.assertEqual(
            my_file.my_func('something'), # actual return value
            'return value', # expected return value
            'an explaination of this test case'
        )

if __name__ == '__main__':
    unittest.main(exit=False)
