import unittest
from unittest.mock import patch
from requests.models import Response
from homework import get_random_cat_image

class TestCatAPI(unittest.TestCase):

    @patch('requests.get')
    def test_successful_request(self, mock_get):
        mock_response = Response()
        mock_response.status_code = 200
        mock_response._content = b'[{"url": "https://example.com/cat.jpg"}]'
        mock_get.return_value = mock_response

        result = get_random_cat_image()
        self.assertEqual(result, "https://example.com/cat.jpg")

    @patch('requests.get')
    def test_unsuccessful_request(self, mock_get):
        mock_response = Response()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_random_cat_image()
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()