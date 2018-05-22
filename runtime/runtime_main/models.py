from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.


class UserInfo(models.Model):

    weight = models.PositiveIntegerField(default=0)

    height = models.PositiveIntegerField(default=0)

    age = models.PositiveIntegerField(default=0)

    food_hours = models.PositiveIntegerField(validators=[
            MaxValueValidator(24),
            MinValueValidator(1)
        ])

    food_calories = models.PositiveIntegerField(default=0)

    active_hours = models.PositiveIntegerField(validators=[
            MaxValueValidator(24),
            MinValueValidator(1)
        ])

    activity_rating = models.PositiveIntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])

    comfort_rating = models.PositiveIntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])

    sleep_hours = models.PositiveIntegerField(validators=[
            MaxValueValidator(24),
            MinValueValidator(1)
        ])

    sleep_duration = models.PositiveIntegerField(validators=[
            MaxValueValidator(24),
            MinValueValidator(1)
        ])

    created = models.DateTimeField(default=datetime.datetime.now())
