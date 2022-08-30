from gettext import Catalog
from random import choices
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    category_log = (
        ("Mental Health", 'Mental Health'),
        ("Heart Disease", 'Heart Disease'),
        ("Covid19", 'Covid19'),
        ("Immunization", 'Immunization'),
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    summary = models.TextField(max_length=200)
    content = models.TextField(max_length=200)
    category = models.TextField(
        max_length=30, choices=category_log)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
