from django.db import models

class FooterSection(models.Model):

    title = models.CharField(max_length=20, default="", blank=True)
    content = models.TextField()

    def __str__(self):
        return 'FooterSection: ' + self.title
