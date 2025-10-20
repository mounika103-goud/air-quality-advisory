import unittest
from src.models.aqi_model import AQIModel
from src.models.advisory_model import AdvisoryModel

class TestAQIModel(unittest.TestCase):
    def test_aqi_initialization(self):
        aqi = AQIModel(value=50, category='Good')
        self.assertEqual(aqi.value, 50)
        self.assertEqual(aqi.category, 'Good')

    def test_aqi_invalid_value(self):
        with self.assertRaises(ValueError):
            AQIModel(value=-1, category='Good')

class TestAdvisoryModel(unittest.TestCase):
    def test_advisory_initialization(self):
        advisory = AdvisoryModel(message='No health concerns', level='Low')
        self.assertEqual(advisory.message, 'No health concerns')
        self.assertEqual(advisory.level, 'Low')

    def test_advisory_invalid_level(self):
        with self.assertRaises(ValueError):
            AdvisoryModel(message='Invalid level', level='Extreme')

if __name__ == '__main__':
    unittest.main()