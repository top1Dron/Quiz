from django.contrib import admin
from .models import Subject, LecturerSubjects


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(LecturerSubjects)
class LectureSubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'lecturer')