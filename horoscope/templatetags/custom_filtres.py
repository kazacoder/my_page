from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='split')
@stringfilter
def split(value, key=' '):
    return value.split(key)


@register.filter(name='times')
def times(value):
    try:
        int(value)
    except:
        raise ValueError('в фильтр times необходимо передавать целое число')
    return '_' * int(value)


@register.filter(name='filter_range')
def filter_range(value, key):
    try:
        int(value)
        int(key)
    except:
        raise ValueError('в фильтр times необходимо передавать целое число')
    return range(int(value), int(key))
