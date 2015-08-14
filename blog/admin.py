from django.contrib import admin
from .models import Post

#map(admin.site.register, [Post])
admin.site.register(Post)
