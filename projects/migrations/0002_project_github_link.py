# Generated by Django 3.0.8 on 2020-09-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.URLField(default=None, max_length=250),
            preserve_default=False,
        ),
    ]
