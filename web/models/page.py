from django.db import models
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):

    title = models.CharField(max_length=20, default="")
    path = models.CharField(max_length=20, default="")
    content = models.TextField(blank=True)
    is_in_menu = models.BooleanField()

    def __str__(self):
        return 'Page: ' + self.title
