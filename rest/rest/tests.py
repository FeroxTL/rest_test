from rest_framework.test import APITestCase
from rest_framework import status


class RestTestCase(APITestCase):
    def test_rest_json_api(self):
        # it works as expected
        response = self.client.post('/api/test/', data=[{}], format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('non_field_errors' in response.data)

    def test_rest_browsable_api(self):
        # it fails with AttributeError
        response = self.client.post('/api/test/?format=api', data=[{}], format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('non_field_errors' in response.data)
