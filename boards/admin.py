from django.contrib import admin
from .models import Board, Post

admin.site.register(Board)  # to display the 'board' app in admin CMS
admin.site.register(Post)  # to display the 'post' app in admin CMS
