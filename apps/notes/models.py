from django.db import models

# Create your models here.


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='snippets')

    class Meta:
        ordering = ('created',)