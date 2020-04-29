# Generated by Django 3.0.5 on 2020-04-27 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_group'),
        ('accounts', '0006_profile_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cathedra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lecturers', to='department.Сathedra', verbose_name='Кафедра'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lecturers', to='department.Faculty', verbose_name='Факультет'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='department.Group', verbose_name='Група'),
        ),
    ]
