from django.db.models import FloatField

from . import widgets


class RateField(FloatField):
    def formfield(self, **kwargs):
        # set default widget to RateFieldWidget
        kwargs['widget'] = widgets.RateFieldWidget
        return super(RateField, self).formfield(**kwargs)
