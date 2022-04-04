from django.db import models

class Work(models.Model):

    title = models.CharField(max_length=30, default="")
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    is_published = models.BooleanField()
    video = models.FileField(default="")
    url = models.CharField(max_length=30, default="")

    def __str__(self):
        return 'Work: ' + self.title




