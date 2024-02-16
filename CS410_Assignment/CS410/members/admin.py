from django.contrib import admin
from .models import student, teach

# Register your models here.
admin.site.register(teach)
admin.site.register(student)