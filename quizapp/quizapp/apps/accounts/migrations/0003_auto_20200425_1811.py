# Generated by Django 3.0.5 on 2020-04-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200425_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Дата народження'),
        ),
    ]
