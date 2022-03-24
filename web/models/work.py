from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings



class Work(models.Model):

    title = models.CharField(max_length=30, default="")
    content = models.TextField(blank=True)
    is_published = models.BooleanField()
    video = models.FileField(default="")
    url = models.CharField(max_length=30, default="")

    def __str__(self):
        return 'Work: ' + self.title




