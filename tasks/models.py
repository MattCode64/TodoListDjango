from django.db import models
from django.utils.text import slugify


class Collection(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


    @classmethod
    def get_default_collection(cls) -> 'Collection':
        collection, _ = cls.objects.get_or_create(name='Défault', slug='_defaut')
        return collection

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)


class Task(models.Model):
    description = models.CharField(max_length=300)
    collections = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
