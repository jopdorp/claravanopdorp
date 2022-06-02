from django.db import models
from web.models.work import Work



class TechnologyIcons(models.Model):

    title = models.CharField(max_length=20, default="", blank=True)
    icon_class = models.CharField(max_length=64, default="", blank=True)
    url = models.CharField(max_length=256, default="", blank=True)
    works = models.ManyToManyField(Work)


    def __str__(self):
        return 'TechnologyIcons: ' + self.title

class TechnologyIconsAbout(models.Model):

    title = models.CharField(max_length=20, default="", blank=True)
    icon_class = models.CharField(max_length=64, default="", blank=True)
    url = models.CharField(max_length=256, default="", blank=True)

    def __str__(self):
        return 'TechnologyIcons: ' + self.title






