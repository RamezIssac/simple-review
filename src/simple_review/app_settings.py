from django.conf import settings
from django.utils.translation import ugettext

"""
RATY_DEFAULTS is used to extendes jQuery.raty defaults,
Below configs are for the images paths and enabling internationalisation/translation on text
"""
RATY_DEFAULTS = {
    'starHalf': '%ssimple_review/vendor/raty/images/star-half.png' % settings.STATIC_URL,
    'starOff': '%ssimple_review/vendor/raty/images/star-off.png' % settings.STATIC_URL,
    'starOn': '%ssimple_review/vendor/raty/images/star-on.png' % settings.STATIC_URL,
    'cancelOff': '%ssimple_review/vendor/raty/images/cancel-off.png' % settings.STATIC_URL,
    'cancelOn': '%ssimple_review/vendor/raty/images/cancel-on.png' % settings.STATIC_URL,
    'hints': [
        ugettext('bad'),
        ugettext('poor'),
        ugettext('regular'),
        ugettext('good'),
        ugettext('gorgeous'),
    ],
    'cancelHint': ugettext("Cancel this rating!"),
    'noRatedMsg': ugettext('Not rated yet!'),
}

RATY_DEFAULTS.update(getattr(settings, 'RATY_DEFAULTS', {}))


# todo
# LOGGED_IN_USERS_ONLY
# JQUERY path
# ALLOW_EMPTY_BODY
