from django.contrib import admin
from .models import Task, Team, User, UserProfile

admin.site.register(Task)
admin.site.register(Team)
admin.site.register(UserProfile)
# Register your models here


