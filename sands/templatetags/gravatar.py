from django import template
from libgravatar import Gravatar


register = template.Library()

@register.filter
def get_gravatar(email):
    return Gravatar(email).get_image(size = 32, default = "identicon", rating = "g")