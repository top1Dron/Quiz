# Generated by Django 3.0.5 on 2020-04-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Назва предмету'),
        ),
    ]
