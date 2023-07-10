from rest_framework import serializers
from .models import BookModel, Authormodel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authormodel
        fields = ('name', 'surname', 'date_birth')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id', 'author', 'name', 'category', 'page', 'price')


