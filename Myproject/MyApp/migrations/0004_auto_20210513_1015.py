# Generated by Django 3.0 on 2021-05-13 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_auto_20210513_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=100)),
                ('pata', models.CharField(max_length=100)),
                ('kala', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='coder',
            name='skill',
            field=models.CharField(default='', max_length=300),
        ),
    ]
