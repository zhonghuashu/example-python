import unittest
import electric_car

class TestElectricCar(unittest.TestCase):
    """Unit test for electric car."""
    
    def setUp(self):
        """Run setup before any other test_xxx() function."""
    
    def test_descriptive_name(self):
        my_tesla = electric_car.ElectricCar('tesla', 'model s', 2019)
        self.assertEqual(my_tesla.get_descriptive_name(), '2019 Tesla Model S')

if __name__ == '__main__':
    unittest.main()