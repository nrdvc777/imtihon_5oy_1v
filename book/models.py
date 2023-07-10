from django.db import models
from datetime import datetime


# Create your models here.

class Authormodel(models.Model):
    name = models.CharField(max_length=77, default='')
    surname = models.CharField(max_length=77, default='')
    date_birth = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'author'


class BookModel(models.Model):
    author = models.ForeignKey(Authormodel, on_delete=models.CASCADE)
    name = models.CharField(max_length=111, default='')
    category = models.CharField(max_length=65, default='')
    page = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'book'
