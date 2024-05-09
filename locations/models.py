from django.db import models


class Locations(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    foto_file = models.ImageField(upload_to='images/locations/')
    address = models.CharField(max_length=255)
    status = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
