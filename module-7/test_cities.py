import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for the function city_country()."""

    def test_city_country(self):
        """city_country('Rio de Janeiro', 'Brazil') -> 'Rio de Janeiro, Brazil'"""
        result = city_country('Rio de Janeiro', 'Brazil')
        self.assertEqual(result, 'Rio de Janeiro, Brazil')


if __name__ == '__main__':
    unittest.main()
