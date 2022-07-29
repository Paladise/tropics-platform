from datetime import datetime
from django.db import models
from django.utils.text import slugify


# A sand will act as a room
class Sand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=200)
    category = models.CharField(max_length=50)
    aka = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

class SandView(models.Model):
    sand = models.ForeignKey(Sand, related_name="sandviews", on_delete=models.CASCADE)
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40)
    created = models.DateTimeField(default=datetime.now())