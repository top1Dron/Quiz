from django.contrib import admin
from .models import Answers, Choices, Questions


@admin.register(Answers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answerName',)


@admin.register(Choices)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'isCorrect', 'points')


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('module', 'questionName')