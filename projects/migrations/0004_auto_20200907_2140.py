# Generated by Django 3.0.8 on 2020-09-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200905_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/projects/img/'),
        ),
    ]
