from rest_framework.test import APITestCase
from rest_framework import status


class RestTestCase(APITestCase):
    def test_rest_list(self):
        response = self.client.post('/api/test/?format=api', data=[{}], format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
