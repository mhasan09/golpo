from django.contrib import admin

# Register your models here.
from .models import POST, UserProfile, Like

admin.site.register(POST)
admin.site.register(UserProfile)
admin.site.register(Like)
