from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('user', 'isLecturer', 'birthdate', 'group', 'faculty', 'cathedra')
