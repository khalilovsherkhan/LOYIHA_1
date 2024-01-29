from django.contrib import admin
from .models import *


# Register your models here.
from django.utils.safestring import mark_safe


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'content', 'sherxonjon', 'data',)
    list_filter = ("date", "name")

admin.site.register(Category)
admin.site.register(Post)