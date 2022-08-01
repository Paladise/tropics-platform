from django.core.validators import MinLengthValidator
from django.db import models
from sands.models import Sand
# from authentication.models import User # commented to prevent circular import error

# A water will act as a post
class Water(models.Model):
    id = models.AutoField(primary_key=True)
    sand = models.ForeignKey(Sand, related_name="waters", on_delete=models.CASCADE)
    author = models.ForeignKey("authentication.User", related_name="waters", on_delete=models.CASCADE) # Prevent circular import error
    content = models.TextField(
            validators = [
                MinLengthValidator(25, 'The field must contain at least 25 characters.')
            ]
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    mangoes = models.IntegerField(default=0)

    class Meta:
        ordering = ("-mangoes", "date_added")
