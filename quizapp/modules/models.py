from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from subjects.models import Subject

    
class Module(models.Model):
    """class that describes module model
    Every subject can have many modules"""

    name = models.CharField(max_length=100)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='modules'
    )


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('subjects:list')


    class Meta:
        ordering = ('name',)


class UserQuiz(models.Model):
    """class that describes UserQuiz model
    This model keep data for every user passage module
    User can pass one module many times"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_quiz'
    )
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='user_quiz'
    )
