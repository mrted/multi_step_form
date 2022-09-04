from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='images/profile_pictures')

    def __str__(self):
        return self.last_name
