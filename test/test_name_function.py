import unittest
from usage import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Unit test name function."""
    
    def test_first_last_name(self):
        formated_name = get_formatted_name("Zhong Hua", "Shu")
        print(formated_name)
        self.assertEqual(formated_name, 'Zhong Hua Shu')

if __name__ == '__main__':
    unittest.main()