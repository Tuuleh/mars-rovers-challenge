from django.db import models


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
    # Enum options for directions
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
