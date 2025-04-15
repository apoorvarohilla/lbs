from django.contrib import admin
from .models import Admin, Book

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    ordering = ('id',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'isbn', 'publication_date', 'genre')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('genre', 'publication_date')
    ordering = ('id',)
