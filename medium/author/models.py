import uuid

from django.db import models

class Author(models.Model):
    id = models.UUIDField("id", primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    picture = models.URLField()

    class Meta:
        verbose_name = ('author')
        verbose_name_plural = ('authors')

    def __str__(self):
        return self.name