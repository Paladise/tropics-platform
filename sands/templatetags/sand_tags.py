from datetime import timedelta
from django.utils import timezone, dateformat
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
    return waters.filter(deleted = False, author__is_banned = False).count()
    
@register.filter
def format_time(time):
    time = timezone.localtime(time)
    cur = timezone.localtime(timezone.now())
    diff = cur - time
    if time.month != cur.month or diff.days > 30:
        if time.year == cur.year:
            return dateformat.format(time, "M j") + " at " + dateformat.format(time, "f A")
        else:
            return dateformat.format(time, "M j, Y") + " at " + dateformat.format(time, "f A")
        
    days = diff.days
    hours = diff.seconds // (60 * 60)
    mins = diff.seconds // 60
    seconds = diff.seconds
    
    if days > 1:
        return f"{days} days ago"
    elif time.day != cur.day:
        return f"yesterday"
    elif hours > 1:
        return f"{hours} hours ago"
    elif hours == 1:
        return f"{hours} hour ago"
    elif mins > 1:
        return f"{mins} minutes ago"
    elif mins == 1:
        return f"{mins} minute ago"
    elif seconds > 1:
        return f"{seconds} seconds ago"
    else:
        return f"{seconds} second ago"
        
    
    