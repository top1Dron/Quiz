# Generated by Django 3.0.5 on 2020-04-25 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200425_2314'),
        ('subjects', '0002_auto_20200423_2153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('name',), 'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
        migrations.CreateModel(
            name='LecturerSubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
            ],
        ),
    ]
