from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content')

    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post,PostAdmin)

admin.site.register(Comment)