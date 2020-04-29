from django.db import models
from modules.models import Module


class Questions(models.Model):
    """class that describes question model
    Every module can have many questions"""

    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    questionName = models.CharField('Питання', max_length=255)


    def __str__(self):
        return self.questionName

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    


class Answers(models.Model):
    """class that describes answers model"""

    answerName = models.CharField('Відповідь', max_length=255)


    def __str__(self):
        return self.answerName
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Choices(models.Model):
    """class that describes choices model
    This model is needed for linking questions and answers. Every right answer costs some points"""

    question = models.ForeignKey(
        Questions,
        on_delete=models.CASCADE,
        related_name='choices'
    )
    answer = models.ForeignKey(
        Answers,
        on_delete=models.SET_NULL,
        blank=True, 
        null=True,
    )
    isCorrect = models.BooleanField('Правильний?', default=False)
    points = models.IntegerField('Кількість баллів', default=0)

    class Meta:
        verbose_name = 'Вопрос - Ответ'
        verbose_name_plural = 'Вопросы - Ответы'