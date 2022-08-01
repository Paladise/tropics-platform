from datetime import timedelta
from django import template


register = template.Library()

@register.filter
def same_time(d1, d2):
    return abs(d1 - d2) < timedelta(seconds=1)