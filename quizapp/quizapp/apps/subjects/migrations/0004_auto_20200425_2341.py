# Generated by Django 3.0.5 on 2020-04-25 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20200425_2314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecturersubjects',
            options={'verbose_name': 'Предмет лектора', 'verbose_name_plural': 'Предмети лекторів'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('name',), 'verbose_name': 'Предмет', 'verbose_name_plural': 'Предмети'},
        ),
    ]
