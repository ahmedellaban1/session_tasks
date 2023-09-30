from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date', 'auther']
    search_fields = ['title']
    list_filter = ['title', 'publish_date', 'auther']


admin.site.register(Post, PostAdmin)

