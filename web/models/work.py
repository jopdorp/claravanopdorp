from django.db import models

class Work(models.Model):

    title = models.CharField(max_length=20, default="")
    content = models.TextField(blank=True)
    is_published = models.BooleanField()

    def __str__(self):
        return 'Work: ' + self.title




