from django.db import models
# from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    foto_file = models.CharField(max_length=255)


# class Recommendation(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     answer1 = models.TextField()
#     answer2 = models.TextField()
#     answer3 = models.TextField()
#     answer4 = models.TextField()
#     answer5 = models.TextField()
#     # title = models.CharField(max_length=100)
#     # description = models.TextField()
#     # foto_file = models.ImageField(upload_to='images/')
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.answer1
