from django.contrib import admin
from . import models

# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = models.Group

admin.site.register(models.Group)
