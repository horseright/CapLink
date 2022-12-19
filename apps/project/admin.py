from django.contrib import admin

from .models import Image, Album, Project, Faq, FaqCategory

# Register your models here.


admin.site.register([Image, Album, Project, Faq, FaqCategory])
