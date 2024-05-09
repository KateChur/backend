from django.db import models
from django.contrib.auth.models import User


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.PROTECT)


class Event(models.Model):
    title = models.CharField(max_length=255)
    description_one = models.TextField()
    foto_one = models.ImageField()
    foto_two = models.ImageField()
    foto_three = models.ImageField()
    foto_four = models.ImageField()

    def __str__(self):
        return self.title


