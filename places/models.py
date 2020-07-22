from django.db import models


class Place(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Place #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'places'

