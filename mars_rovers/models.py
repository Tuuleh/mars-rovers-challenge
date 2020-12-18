from django.core.exceptions import ValidationError
from django.db import models
import re


class Plane(models.Model):
    """
    A representation of the plane that the Mars Rovers travel across, with height and width
    """
    height = models.IntegerField()
    width = models.IntegerField()


class Rover(models.Model):
    """
    A single Mars Rover on a specific plane, created for a specific user
    """

    # I want directions to be an enumerable, since only N,S,E and W are valid alternatives
    class Directions(models.TextChoices):
        NORTH = 'N',
        SOUTH = 'S',
        EAST = 'E',
        WEST = 'W',

    direction = models.CharField(
        max_length=1,
        choices=Directions.choices,
        default=Directions.NORTH
    )

    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)

    latitude = models.IntegerField()
    longitude = models.IntegerField()

    def process_command(self, command):
        # Throw if the command contains any other letters than M, L or R - that makes it invalid
        regex = r'[^MLR]'
        if re.search(regex, command):
            raise ValidationError(
                'Invalid rover command - the rover command code must only include letters M, L or R',
                code='invalid'
            )
        for step in command:
            print(step)
            if step == 'M':
                self.move()
            else:
                self.rotate(step)
        return

    def rotate(self, direction):
        """ Change the direction the rover is facing based on the instruction to turn (either 'L' or 'R') """
        valid_directions = ('N', 'E', 'S', 'W')
        current_bearing_index = valid_directions.index(self.direction)
        if direction == "L":
            new_bearing_index = (current_bearing_index - 1)
        else:
            new_bearing_index = (current_bearing_index + 1)
        new_bearing_index %= len(valid_directions)
        self.direction = valid_directions[new_bearing_index]
        print("self", self)
        return self

    def move(self):
        """
        Move the rover one unit towards the direction it's facing.
        """
        if self.direction == "N":
            self.longitude += 1
        elif self.direction == "S":
            self.longitude -= 1
        elif self.direction == "E":
            self.latitude -= 1
        else:
            self.latitude += 1
        return self
