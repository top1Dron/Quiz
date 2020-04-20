from modules.models import Module
from .forms import QuestionForm, AnswerForm, ChoicesForm
from .models import Answers, Choices, Questions

class QuizServices:
    def getModules(self, moduleId):
        return Module.objects.filter(pk=moduleId)[0]

    def postCreateQuizChoice(self, request):
        questionForm = QuestionForm(data=request.POST)

        answerForm1 = AnswerForm(data=request.POST, prefix='first')
        choicesForm1 = ChoicesForm(data=request.POST, prefix='first')

        answerForm2 = AnswerForm(data=request.POST, prefix='second')
        choicesForm2 = ChoicesForm(data=request.POST, prefix='second')

        answerForm3 = AnswerForm(data=request.POST, prefix='third')
        choicesForm3 = ChoicesForm(data=request.POST, prefix='third')

        answerForm4 = AnswerForm(data=request.POST, prefix='fourth')
        choicesForm4 = ChoicesForm(data=request.POST, prefix='fourth')
        

        if questionForm.is_valid() and \
        answerForm1.is_valid() and choicesForm1.is_valid() and \
        answerForm2.is_valid() and choicesForm2.is_valid() and \
        answerForm3.is_valid() and choicesForm3.is_valid() and \
        answerForm4.is_valid() and choicesForm4.is_valid(): 

            questionForm.instance.module = self.module
            newQuestion = questionForm.save()

            newAnswer = answerForm1.save()
            choicesForm1.instance.question = newQuestion
            choicesForm1.instance.answer = newAnswer
            choicesForm1.save()

            newAnswer = answerForm2.save()
            choicesForm2.instance.question = newQuestion
            choicesForm2.instance.answer = newAnswer
            choicesForm2.save()

            newAnswer = answerForm3.save()
            choicesForm3.instance.question = newQuestion
            choicesForm3.instance.answer = newAnswer
            choicesForm3.save()

            newAnswer = answerForm4.save()
            choicesForm4.instance.question = newQuestion
            choicesForm4.instance.answer = newAnswer
            choicesForm4.save()


    def getCreateQuizChoice(self, request):
        questionForm = QuestionForm()
        
        answerForm1 = AnswerForm(prefix='first')
        choicesForm1 = ChoicesForm(prefix='first')

        answerForm2 = AnswerForm(prefix='second')
        choicesForm2 = ChoicesForm(prefix='second')

        answerForm3 = AnswerForm(prefix='third')
        choicesForm3 = ChoicesForm(prefix='third')

        answerForm4 = AnswerForm(prefix='fourth')
        choicesForm4 = ChoicesForm(prefix='fourth')
        return (questionForm, answerForm1, choicesForm1,
                            answerForm2, choicesForm2,
                            answerForm3, choicesForm3,
                            answerForm4, choicesForm4)    