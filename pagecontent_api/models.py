from django.db import models


class PressContent(models.Model):
    label = models.CharField(null=False, blank=False, max_length=50)
    url = models.URLField()
    date = models.DateTimeField(null=False) # Published Date
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='presscontent'
        verbose_name='Presscontent'
        verbose_name_plural = 'PressContents'

    def __str__(self):
        return self.label
