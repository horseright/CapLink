from django.contrib import admin

from .models import Order, Output

# Register your models here.


admin.site.register([Order])
admin.site.register([Output])
