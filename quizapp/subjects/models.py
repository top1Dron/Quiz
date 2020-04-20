from django.db import models
from django.shortcuts import reverse


class Subject(models.Model):
    """class that describes subject model"""

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


    def __unicode__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('subjects:list')


    class Meta:
        ordering = ('name',)
