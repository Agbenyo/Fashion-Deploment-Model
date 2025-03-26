import unittest
from src.datasets import load_data  # Replace with your actual data loading function

class TestDataLoading(unittest.TestCase):

    def test_load_data(self):
        data = load_data('https://www.kaggle.com/code/gpreda/cnn-with-tensorflow-keras-for-fashion-mnist')
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)  # Ensure data is not empty

if __name__ == '__main__':
    unittest.main()
