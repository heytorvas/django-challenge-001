import uuid
from django.db import models
from django.db.models.fields import related
from author.models import Author

# Create your models here.
class Article(models.Model):
    id = models.UUIDField("id", primary_key=True, editable=False, default=uuid.uuid4)
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    first_paragraph = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE, db_column='author')

    def __str__(self):
        return self.title