import unittest
from flask import json
from src.app import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_advisory_endpoint(self):
        response = self.app.post('/advisory', 
                                  data=json.dumps({'aqi': 75, 'group': 'Children'}),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('aqi_category', response.json)
        self.assertIn('advice', response.json)

    def test_advisory_endpoint_invalid_aqi(self):
        response = self.app.post('/advisory', 
                                  data=json.dumps({'aqi': 600}),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['aqi_category'], 'Unknown')
        self.assertEqual(response.json['advice'], 'AQI value out of range. Please check the input.')

    def test_advisory_endpoint_missing_aqi(self):
        response = self.app.post('/advisory', 
                                  data=json.dumps({'group': 'Elderly'}),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('aqi_category', response.json)
        self.assertIn('advice', response.json)

if __name__ == '__main__':
    unittest.main()