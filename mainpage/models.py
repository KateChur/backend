from django.db import models
from django.contrib.auth.models import User
from locations.models import Locations
# from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)


# class Locations(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     address = models.CharField(max_length=255)
#     status = models.BooleanField()
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name


class Event_item(models.Model):
    class Meta:
        ordering = ["-date_created"]

    # slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    foto_file = models.ImageField(upload_to='images/')
    price = models.DecimalField(decimal_places=10, max_digits=20)
    location = models.ManyToManyField(Locations, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# # Table events {
# #  id integer [pk, increment, unique]
# #  title varchar
# #  description text
# #  image blob
# #   price decimal
# #  created_at datetime
# #  updated_at datetime
# # }


# # Table locations {
# #  id integer [pk, increment, unique]
# #  name varchar
# #  address varchar
# #  status bool
# #  created_at varchar
# #  updated_at varchar
# # }
#
#
# class AvailableDays(models.Model):
#     location = models.ForeignKey(Locations, on_delete=models.CASCADE)
#     date = models.DateField()
#     status = models.BooleanField()
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#
#
# # Table AvailableDays {
# #  id integer [pk, increment, unique]
# #  location_id integer
# #  date datetime
# #   status bool
# # }
# class TimeSlots(models.Model):
#     day = models.ForeignKey(AvailableDays, on_delete=models.CASCADE)
#     begin = models.TimeField()
#     end = models.TimeField()
#     status = models.BooleanField()
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#
#
# # Table timeslots {
# #  id integer [pk, increment, unique]
# #  day_id integer
# #  begin_hour time
# #  end_hour time
# #  status bool
# #   created_at varchar
# #  updated_at varchar
# # }
# class Users(models.Model):
#     login = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255)
#     email = models.EmailField()
#     phone = models.CharField(max_length=255)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#
#
# # Table users {
# #  id integer [pk, increment, unique]
# #  login varchar
# #  password varchar
# #  name integer
# #  surname varchar [null]
# #  mail varchar
# #  phone varchar
# #   created_at varchar
# #  updated_at varchar
# # }
# class Orders(models.Model):
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     event_title = models.ForeignKey(Event_item.title, on_delete=models.CASCADE)
#     event_date = models.DateField()
#     event_price = models.ForeignKey(Event_item.price, on_delete=models.CASCADE)
#     order_date = models.DateField(auto_now_add=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#
# # Table orders {
# #  id integer [pk, increment, unique]
# #  user_id integer
# #  event_title varchar
# #  event_date datetime
# #  event_price decimal
# # order_date datetime
# #   created_at varchar
# #  updated_at varchar
# # }
# #
# # Table events_locations {
# #   event_id int
# #   location_id int
# # }

