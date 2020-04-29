from django.contrib import admin
from .models import Faculty, Сathedra, Group

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Сathedra)
class СathedraAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )