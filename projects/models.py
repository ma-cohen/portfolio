from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=60)
    image = models.CharField(max_length=100)
    github_link = models.URLField(default=None, max_length=250)
