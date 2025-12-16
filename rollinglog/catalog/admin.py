from django.contrib import admin
from .models import Brand, LogEntry, Review, Product


# Register your models here.

admin.site.register(Brand)
admin.site.register(LogEntry)
admin.site.register(Review)
admin.site.register(Product)
