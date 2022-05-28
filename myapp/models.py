from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    slug = models.SlugField(db_column='slug', blank=False, unique=True)

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title