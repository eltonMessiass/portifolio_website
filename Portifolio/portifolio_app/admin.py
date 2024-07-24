from django.contrib import admin

# Register your models here.
from .models import Project, Tools


admin.site.register(Project)
admin.site.register(Tools)

