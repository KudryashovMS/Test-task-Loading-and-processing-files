from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


class FileUploadTests(APITestCase):

    def test_upload_file(self):
        url = '/upload/'
        with open('test_file.txt', 'rb') as file:
            response = self.client.post(url, {'file': file})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_files(self):
        url = '/files/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_upload_malicious_file(self):
        url = '/upload/'
        with open('test_file.jar', 'rb') as file:
            response = self.client.post(url, {'file': file})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
