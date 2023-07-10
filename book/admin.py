from django.contrib import admin
from .models import BookModel, Authormodel

# Register your models here.

admin.site.register(BookModel)
admin.site.register(Authormodel)
