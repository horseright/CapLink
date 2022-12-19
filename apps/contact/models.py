from django.db import models

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField(null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.email
