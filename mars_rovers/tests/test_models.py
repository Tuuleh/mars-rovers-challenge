from django.core.exceptions import ValidationError
from django.test import TestCase
from ..models import Plane, Rover
from django.contrib.auth.models import User


class RoverTest(TestCase):
    """ Test module for the Rover model """

    def setUp(self):
        Rover.objects.create(
            plane=Plane.objects.create(height=5, width=5),
            owner=User.objects.create_user(username='testuser', password='12345'),
            direction="E",
            latitude=3,
            longitude=3
        )

    def test_process_valid_command(self):
        """
        Test that when processing a command, the rover's position changes as expected
        """
        rover = Rover.objects.last()
        command = "MMRMMRMRRM"
        rover.process_command(command)
        self.assertEqual(rover.longitude, 5)
        self.assertEqual(rover.latitude, 1)
        self.assertEqual(rover.direction, "E")

    def test_process_invalid_command(self):
        """
        Test that when we pass an invalid command, we throw a useful validation error
        """
        rover = Rover.objects.last()
        self.assertRaises(ValidationError, rover.process_command, 'blerg')
