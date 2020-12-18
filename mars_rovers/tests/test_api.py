from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient

import json

with open('mars_rovers/tests/fixtures/valid_input.json') as f:
    valid_input = json.load(f)

with open('mars_rovers/tests/fixtures/valid_output.json') as f:
    valid_output = json.load(f)


class RoverDeploymentTests(APITestCase):
    def setUp(self):
        self.username = 'kittykat'
        self.password = 'password'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_deploy_rover(self):
        """ full test case for a valid call to the rover deployment api endpoint """
        self.client.login(username=self.username, password=self.password)
        resp = self.client.post('/rovers/deploy/', valid_input, format='json')
        self.assertEqual(resp.data, valid_output)
