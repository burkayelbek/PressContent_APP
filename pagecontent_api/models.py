from django.db import models
from django.utils.text import slugify


class PressContent(models.Model):
    label = models.CharField(null=False, blank=False, max_length=255)
    url = models.SlugField(unique=True, editable=False, max_length=255)
    date = models.DateTimeField(null=False) # Published Date
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='presscontent'
        verbose_name='Presscontent'
        verbose_name_plural = 'PressContents'

    def get_url(self):
        date = self.date.strftime("%Y/%m/%d")
        url = '{}/{}'.format(date, slugify(self.label.replace("ı", "i")))
        unique = url
        number = 1
        while PressContent.objects.filter(url=unique).exists():
            unique = '{}-{}'.format(url, number)
            number += 1
        return unique

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.url = self.get_url()
        return super(PressContent, self).save(*args, **kwargs)
