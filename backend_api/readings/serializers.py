from rest_framework import serializers
from readings.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        Model = Book
        field  = [
            'title',
            'author',
            'genre',
            'published_year',
            'isbn',
            'publisher',
            'pages',
            'language',
            'description',
            'cover_image',
            'status'
        ] 