from django import template

register = template.Library()

@register.filter(name='my_cut')
def my_cut(value, arg):
    """
    This cuts out values of "arg" from the string!
    """
    return value.replace(arg, '')
