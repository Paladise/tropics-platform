from datetime import datetime
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

# from authentication.models import User # Commented to prevent circular import error


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
    session = models.CharField(max_length=40)
    
class SandTeacher(models.Model):
    sand = models.ForeignKey(Sand, related_name="teachers", on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100,
                validators = [
                    MinLengthValidator(5, 'The field must contain at least 5 characters.')
                ])
    fcps_email = models.EmailField(max_length=100, null=True, blank=True)
    added_by = models.ForeignKey("authentication.User", related_name="added_teachers", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.display_name