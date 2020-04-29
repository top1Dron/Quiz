from django.db import models

class Faculty(models.Model):
    """class that describes faculty"""

    name = models.CharField('Назва факультету', max_length=150)


    def __str__(self):
        return self.name
        
        
    class Meta:
        ordering = ('name', )
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультети'


class Сathedra(models.Model):
    """class that describes faculty"""

    name = models.CharField('Назва кафедри', max_length=150)
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE, related_name='cathedras')


    def __str__(self):
        return self.name


    class Meta:
        ordering = ('name', )
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедри'


class Group(models.Model):
    """class that describes student group"""

    name = models.CharField('Назва групи', max_length=10)
    cathedra = models.ForeignKey(
        to=Сathedra,
        on_delete=models.CASCADE,
        related_name='groups'
    )

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'