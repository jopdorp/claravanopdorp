from django.db import models
from web.models.page import Page
from django_quill.fields import QuillField


class PageSection(models.Model):

    title = models.CharField(max_length=20, default="",blank=True)
    content = QuillField(blank=True, default=None)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return 'PageSection: ' + self.title
