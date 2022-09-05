from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(upload_to='images/profile_pictures')
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.last_name
