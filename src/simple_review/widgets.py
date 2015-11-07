from django.utils.safestring import mark_safe
import simplejson as json
from django import forms
from django.forms import Widget
from django.utils import translation
from django.utils.translation import get_language_info
from . import app_settings


class RateFieldWidget(Widget):
    def _media(self):
        lang = get_language_info(translation.get_language())
        css = {
            'all': ('simple_review/vendor/raty/jquery.raty.css',)
        }
        if lang['bidi']:
            css['all'] = css['all'] + ('simple_review/raty.rtl.css',)
        return forms.Media(css=css,
                           js=('simple_review/vendor/raty/jquery.raty.js',
                               'simple_review/raty_init.js'))

    media = property(_media)

    def render(self, name, value, attrs=None):
        return '<div class="simple-review-raty" scoreName="%s" data-score="%s"></div> %s' \
               % (name, value, self.get_raty_defaults())

    def get_raty_defaults(self):
        defaults = app_settings.RATY_DEFAULTS
        assignment = ' $.extend($.fn.raty.defaults, %s)' % json.dumps(defaults)
        return mark_safe('<script> %s </script>' % (assignment,))
