from django.contrib import admin

from webapp.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'text', 'created_at', 'updated_at', 'statuses')


admin.site.register(Book, BookAdmin)


