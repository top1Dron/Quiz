from accounts.models import Profile
from django.db import models
from django.shortcuts import reverse


class Subject(models.Model):
    """class that describes subject model"""

    name = models.CharField('Назва предмету', max_length=80)

    def __str__(self):
        return self.name


    def __unicode__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('subjects:list')


    class Meta:
        ordering = ('name',)
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмети'


class LecturerSubjects(models.Model):
    """class that describes subjects and lectures, who lead them"""

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
    )
    lecturer = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Предмет лектора'
        verbose_name_plural = 'Предмети лекторів'