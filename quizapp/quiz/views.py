from django.shortcuts import render, redirect, reverse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from .forms import QuestionForm, AnswerForm, ChoicesForm
from .models import Answers, Choices, Questions
from .services import QuizServices

services = QuizServices()


def getModuleAndRedirect(request, pk):
    """view to get module id and redirect to create choice"""

    services.module = services.getModules(pk)
    return redirect(reverse("quiz:create"))


class ChoiceCreate(View):
    """class base view for creating new choice"""

    def get(self, request, *args, **kwargs):
        
        questionForm, answerForm1, choicesForm1, \
            answerForm2, choicesForm2, \
            answerForm3, choicesForm3, \
            answerForm4, choicesForm4 = services.getCreateQuizChoice(request)
        
        return render(request, 'quiz/create.html', {
            'questionForm': questionForm,

            'answerForm1': answerForm1,
            'choicesForm1': choicesForm1,

            'answerForm2': answerForm2,
            'choicesForm2': choicesForm2,

            'answerForm3': answerForm3,
            'choicesForm3': choicesForm3,

            'answerForm4': answerForm4,
            'choicesForm4': choicesForm4,

            'module': services.module
        })


    def post(self, request, *args, **kwargs):
        executed = services.postCreateQuizChoice(request)
        return redirect('subjects:list')