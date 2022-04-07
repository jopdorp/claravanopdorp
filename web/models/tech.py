from django.db import models
from web.models.work import Work


class TechnologyIcons(models.Model):

    title = models.CharField(max_length=20, default="", blank=True)
    content = models.TextField()
    works = models.ManyToManyField(Work)

    def __str__(self):
        return 'TechnologyIcons: ' + self.title
