import pdb
from django import template
from django.utils.safestring import mark_safe
from ..widgets import RateFieldWidget
register = template.Library()

@register.simple_tag
def print_raty(review_instance):
    w = RateFieldWidget()
    return mark_safe(w.render('', review_instance.rate))
