from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "language", "userRating")
  
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
