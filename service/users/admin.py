from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'birthday_year', 'published', 'changed', )
    list_display_links = ('username', 'first_name', 'last_name', )
    search_fields = ('username', 'first_name', 'last_name', )


admin.site.register(User, UserAdmin)
