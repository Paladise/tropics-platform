from django import template


register = template.Library()

@register.filter
def user_gave_mango(user, water):
    return user.gave_mangoes.filter(id = water.id).exists()

@register.filter
def user_can_moderate(user, author):
    return author.id == user.id or user.has_management_permission()