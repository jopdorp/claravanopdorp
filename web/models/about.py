from django.db import models
from django_quill.fields import QuillField

class About(models.Model):

    title = models.CharField(max_length=20, default="")
    intro = models.TextField(blank=True)

    def __str__(self):
        return 'Page: ' + self.title


class AboutSection(models.Model):

    title = models.CharField(max_length=20, default="",blank=True)
    contain = QuillField(blank=True, default=None)
    details = models.TextField(blank=True)
    video = models.FileField(default="", blank=True, null=True)
    url = models.CharField(max_length=256, default="", blank=True, null=True)
    page = models.ForeignKey(About, on_delete=models.CASCADE)
    photo = models.ImageField(default="", blank=True, null=True)

    def __str__(self):
        return 'AboutSection: ' + self.title


