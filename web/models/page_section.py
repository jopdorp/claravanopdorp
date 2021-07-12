from django.db import models
from web.models.page import Page

class PageSection(models.Model):

    title = models.CharField(max_length=20, default="")
    content = models.TextField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return 'PageSection: ' + self.title
