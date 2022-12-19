from django.db import models
from django.contrib.auth.views import get_user_model
from django.conf import settings

# Create your models here.


class AMl(models.Model):
    COUNTRY_CHOICES = (
        ('USA', 'USA'),
        ('CHINA', 'CHINA')
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    country = models.CharField(max_length=255, choices=COUNTRY_CHOICES)
    address = models.CharField(max_length=255)
    post_code = models.IntegerField()

    identification = models.FileField()
    address_proof = models.FileField()

    is_success = models.BooleanField(default=False)

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)
