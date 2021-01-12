from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, db_index=True)
    author_name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True, db_index=True)

    def get_absolute_url(self):
        return reverse('book_detail_url', kwargs={'id': self.id})

    def __str__(self):
        return self.title
