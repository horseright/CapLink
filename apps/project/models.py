from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
from django.urls import reverse


class Album(models.Model):
    name = models.CharField(max_length=255)


class Image(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='imgs')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=4)
    mint = models.DateTimeField(null=True, blank=True)
    owner = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FaqCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    category = models.ForeignKey(FaqCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Project(models.Model):
    title = models.CharField(max_length=255)
    longth = models.IntegerField(validators=(MinValueValidator(0), ))
    hash_rate = models.IntegerField(validators=(MinValueValidator(0), ))
    power = models.IntegerField(validators=(MinValueValidator(0), ))
    efficiency = models.IntegerField(validators=(MinValueValidator(0), ))
    price = models.DecimalField(max_digits=9, decimal_places=4)
    stock = models.IntegerField(validators=(MinValueValidator(0), ))
    sold = models.IntegerField(validators=(MinValueValidator(0), ))

    electricity_fee = models.DecimalField(max_digits=9, decimal_places=4)
    hashrate_fee = models.DecimalField(max_digits=9, decimal_places=4)
    service_fee = models.DecimalField(max_digits=9, decimal_places=4)

    static_revenue_rate = models.ImageField(upload_to='revenue_rate')
    static_breakeven_days = models.ImageField(upload_to='breakeven_days')

    img = models.ImageField(upload_to='projects')
    details = models.ImageField(upload_to='details')
    disclaimers = models.TextField()
    estimated_starting_hours = models.IntegerField(default=72)
    faqs = models.ManyToManyField(Faq, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project:detail', kwargs={'pk': self.pk})
