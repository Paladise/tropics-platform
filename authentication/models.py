from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from waters.models import Water


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    full_name = models.CharField(max_length=50, null=False)
    graduation_year = models.IntegerField(default=0, null=False)
    is_teacher = models.BooleanField(default=False, null=False)
    is_student = models.BooleanField(default=True, null=False)
    is_banned = models.BooleanField(default=False, null=False)
    gave_mangoes = models.ManyToManyField(Water, blank=True) # Blank for admin interface

    @property
    def has_management_permission(self):
        return self.is_teacher or self.is_staff or self.is_superuser


    @property
    def short_name(self):
        return self.username


    @property
    def qualification(self):
        current_year = datetime.now().year
        res = self.graduation_year - current_year

        if int(datetime.now().strftime('%m')) >= 7: # Check if during/after July
            res -= 1

        if res < 0:
            return "Alumni"
        elif res == 0:
            return "Senior"
        elif res == 1:
            return "Junior"
        elif res == 2:
            return "Sophomore"
        elif res == 3:
            return "Freshman"


    def get_social_auth(self):
        return self.social_auth.get(provider="ion")


    def __str__(self):
        return self.short_name