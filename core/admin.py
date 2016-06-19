from django.contrib import admin

# Register your models here.
from .models import *


class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'desc']

class DescriptionAdmin(admin.ModelAdmin):
	fields = ['name', 'flag']

admin.site.register(User, UserAdmin)
admin.site.register(Description, DescriptionAdmin)