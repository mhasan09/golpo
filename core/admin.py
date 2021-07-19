from django.contrib import admin

# Register your models here.
from .models import POST, UserProfile

admin.site.register(POST)
admin.site.register(UserProfile)
