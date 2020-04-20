from django import forms
from .models import Questions, Answers, Choices


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        exclude = ('module',)
        fields = ('questionName',)
        labels = {'Питання':'QuestionName',}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ('answerName',)
        labels = {'Варіант відповіді':'AnswerName',}


class ChoicesForm(forms.ModelForm):
    class Meta:
        model = Choices
        fields = ('isCorrect', 'points',)
        exclude = ('question', 'answer',)
        labels = {'Правильний':'IsCorrect', 'Кількість балів': 'Points',}