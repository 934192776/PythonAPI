from django.contrib import admin

# Register your models here.
from django.contrib import admin

from blog.models import (Category, Post,
                         Comment, Profile)

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
