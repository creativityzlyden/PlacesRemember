from django.db import models


class Place(models.Model):
    text = models.TextField("Описание", blank=True)
    image = models.ImageField("Фото", upload_to="photo/", blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Место #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'Места'
