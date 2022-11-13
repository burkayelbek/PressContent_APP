from django.db import models
from django.utils.text import slugify
from rest_framework.reverse import reverse
from django.contrib.sites.shortcuts import get_current_site


class PressContent(models.Model):
    label = models.CharField(null=False, blank=False, max_length=255)
    slug = models.SlugField(unique=True, editable=False, max_length=255)
    date = models.DateTimeField(null=False) # Published Date
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='presscontent'
        verbose_name='Presscontent'
        verbose_name_plural = 'PressContents'

    def __str__(self):
        return self.label

    def get_slug(self):
        date = self.date.strftime("%Y-%m-%d")
        slug = '{}-{}'.format(date, slugify(self.label.replace("ı", "i")))
        unique = slug
        number = 1
        while PressContent.objects.filter(slug=unique).exists():
            unique = '{}-{}'.format(slug, number)
            number += 1
        return unique



    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        return super(PressContent, self).save(*args, **kwargs)

    def get_current_site(self, request, **kwargs):
        return 'http://{}/api/detail/{}'.format(get_current_site(request), self.slug)
