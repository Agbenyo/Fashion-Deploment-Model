import unittest
import requests

class TestIntegration(unittest.TestCase):

    base_url = 'http://127.0.0.1:8000'  # Replace with your actual URL

    def test_root_endpoint(self):
        response = requests.get(f'{self.base_url}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_predict_endpoint(self):
        image_data = ...  # Prepare your image data
        response = requests.post(f'{self.base_url}/predict', json={'image': image_data})
        self.assertEqual(response.status_code, 200)
        self.assertIn('predictions', response.json())

if __name__ == '__main__':
    unittest.main()
