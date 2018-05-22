from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class MyUser(models.Model):

    f_name = models.CharField(max_length=56)

    l_name = models.CharField(max_length=56)

    email = models.EmailField()

    def __str__(self):
        return self.f_name + ' ' + self.l_name


class UserInfo(models.Model):

    user = models.ForeignKey(MyUser,
                             related_name='user_info',
                             on_delete=models.CASCADE)

    weight = models.PositiveIntegerField(default=0)

    height = models.PositiveIntegerField(default=0)

    age = models.PositiveIntegerField(default=0)

    food_hours = models.PositiveIntegerField(validators=[
            MaxValueValidator(24),
            MinValueValidator(1)
        ])

    food_calories = models.PositiveIntegerField(default=0)

    active_hours = models.PositiveIntegerField(validators=[
            MaxValueValidator(10),
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
