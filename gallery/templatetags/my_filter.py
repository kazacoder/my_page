from os.path import exists
from django import template

register = template.Library()


@register.filter(name='check_path')
def check_path(value):
    return exists(value)
