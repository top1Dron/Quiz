# Generated by Django 3.0.5 on 2020-04-28 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_auto_20200427_2005'),
        ('accounts', '0011_auto_20200427_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='department.Group', verbose_name='Група'),
        ),
    ]
