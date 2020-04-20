from django.contrib import admin
from .models import Module, UserQuiz


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


@admin.register(UserQuiz)
class UserQuizAdmin(admin.ModelAdmin):
    list_display = ('user', 'module')