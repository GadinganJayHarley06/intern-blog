from django.contrib import admin
from .models import Post, Index, Category, Tag
admin.site.register(Post)
admin.site.register(Index)
admin.site.register(Category)
admin.site.register(Tag)