from django.db import models
from django.contrib.postgres.fields import ArrayField

class Filme(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, default='')
    palavras = models.TextField()
    def __str__(self):
        return f"{self.title}"