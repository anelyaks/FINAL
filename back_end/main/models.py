from django.db import models
from django.urls import reverse


class Articles(models.Model):
    name = models.CharField('name', max_length=50, db_index=True)
    email = models.CharField('email', max_length=250)
    subject = models.CharField('subject', max_length=250)
    message = models.TextField('message')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'





