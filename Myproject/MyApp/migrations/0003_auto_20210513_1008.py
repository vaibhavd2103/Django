# Generated by Django 3.0 on 2021-05-13 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_coder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coder',
            name='price',
        ),
        migrations.AddField(
            model_name='coder',
            name='skill',
            field=models.CharField(default='enter skills', max_length=300),
        ),
    ]