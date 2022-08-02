from datetime import timedelta
from django import template
from libgravatar import Gravatar
register = template.Library()

@register.filter
def gave_mango(user, water):
    return user.gave_mangoes.filter(id = water.id).exists()

@register.filter
def can_moderate(user, author):
    return author.id == user.id or user.has_management_permission
    
@register.filter
def same_time(d1, d2):
    return abs(d1 - d2) < timedelta(seconds=1)
    
@register.filter
def get_gravatar(email):
    return Gravatar(email).get_image(size = 32, default = "identicon", rating = "g")
    
@register.filter
def count_waters(waters):
    return waters.filter(deleted = False).count()