from django.db import models


class Order(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    day = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.id
