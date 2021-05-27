from django.db import models

# Create your models here.


class JobApplication(models.Model):
    fname = models.CharField(max_length=200, blank=True)
    lname = models.CharField(max_length=200, blank=True)
    designation = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    mail = models.EmailField(max_length = 254)
    city = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=200, blank=True)
    zip = models.CharField(max_length=200, blank=True)
    relation_status = models.CharField(max_length=200, blank=True)
    dob = models.DateField(max_length=200, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
            return self.fname + ' ' +self.lname