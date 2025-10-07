from django.contrib import admin
from .models import Book, Author, Publisher

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publisher', 'price', 'created_at']
    list_filter = ['author', 'publisher', 'created_at']
    search_fields = ['title', 'author__name', 'publisher__name']
