from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Bill, Item

admin.site.register(Item)
admin.site.register(Bill)
