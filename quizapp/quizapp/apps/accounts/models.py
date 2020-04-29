from department.models import Faculty, Сathedra, Group
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """Additional information about User"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isLecturer  = models.BooleanField('Ви вчитель?', default=False)
    birthdate = models.DateField('Дата народження', blank=True, null=True)
    faculty = models.ForeignKey(
        verbose_name='Факультет',
        to=Faculty,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='lecturers'
    )
    cathedra = models.ForeignKey(
        verbose_name='Кафедра',
        to=Сathedra,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='lecturers'
    )
    group = models.ForeignKey(
        verbose_name='Група',
        blank=True,
        to=Group,
        null=True,
        on_delete=models.SET_NULL,
        related_name='students'
    )



    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'