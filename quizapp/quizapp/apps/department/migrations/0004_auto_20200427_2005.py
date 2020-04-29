# Generated by Django 3.0.5 on 2020-04-27 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Група', 'verbose_name_plural': 'Групи'},
        ),
        migrations.AlterField(
            model_name='group',
            name='cathedra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='department.Сathedra'),
        ),
    ]
