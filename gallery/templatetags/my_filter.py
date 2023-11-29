

from django import template
from django.core.validators import URLValidator
from django.http import request

register = template.Library()


@register.filter(name='check_url')
def check_url(value):
    val = request.GET.get(value, None)
    return val
