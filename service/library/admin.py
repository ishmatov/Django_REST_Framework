from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday_year', )
    list_display_links = ('first_name', 'last_name', 'birthday_year', )
    search_fields = ('first_name', 'last_name', 'birthday_year', )


admin.site.register(Author, AuthorAdmin)
