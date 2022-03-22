from django.db import models
from django_quill.fields import QuillField

class Page(models.Model):

    title = models.CharField(max_length=20, default="")
    path = models.CharField(max_length=20, default="")
    content = models.TextField(blank=True)
    is_in_menu = models.BooleanField()

    def __str__(self):
        return 'Page: ' + self.title


class PageSection(models.Model):

    title = models.CharField(max_length=20, default="",blank=True)
    content = QuillField(blank=True, default=None)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return 'PageSection: ' + self.title


