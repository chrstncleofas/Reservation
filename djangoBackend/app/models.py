from django.db import models

class Reservation(models.Model):
    userID = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    class Meta:
        ordering = ['userID']
