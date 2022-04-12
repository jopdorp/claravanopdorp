from django.db import models
from django_quill.fields import QuillField


class Work(models.Model):

    title = models.CharField(max_length=30, default="")
    description = models.CharField(max_length=500, default="",blank=True)
    content = models.TextField(blank=True)
    is_published = models.BooleanField()
    video = models.FileField(default="")
    url = models.CharField(max_length=256, default="")
    github_url = models.CharField(max_length=256, default="")

    def __str__(self):
        return 'Work: ' + self.title

class WorkSection(models.Model):

    title = models.CharField(max_length=20, default="",blank=True)
    reference = models.TextField(blank=True)
    content = QuillField(default="", blank=True, null=True)
    photo = models.ImageField(default="", blank=True, null=True)
    url = models.CharField(max_length=256, default="", blank=True, null=True)
    feet = models.TextField(blank=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)

    def __str__(self):
        return 'WorkSection: ' + self.title






