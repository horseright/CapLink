from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Order(models.Model):
    STATUS_CHOICES = (
        ('normal', 'normal'),
        ('repair', 'repair'),
        ('waiting', 'waiting'),
        )

    order_id = models.UUIDField(default=uuid4, unique=True)
    service_product = models.CharField(max_length=255)
    pool = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    longth = models.IntegerField(validators=(MinValueValidator(0),))
    output = models.DecimalField(max_digits=9, decimal_places=4)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)

    @property
    def residual_time(self):
        pass

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'orders'


class Output(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='production')

    date = models.CharField(max_length=255)
    pool = models.CharField(max_length=255)
    production = models.DecimalField(max_digits=9, decimal_places=4)

    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date
