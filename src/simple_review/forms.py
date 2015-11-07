import pdb
from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import Review


class SimpleReviewForm(forms.ModelForm):
    goto = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        fields = ('rate', 'body', 'user', 'object_id', 'content_type')
        model = Review
        widgets = {
            'user': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
            'content_type': forms.HiddenInput(),
        }

    def patch_form(self, request, model):
        '''
        Edit the form fields to include by default the user, content_type, object_id, and goto(next)
        :param request:
        :param model:
        :return: the patched form
        '''
        self.fields['user'].initial = request.user if not request.user.is_anonymous() else ''
        self.fields['object_id'].initial = '%s' % model.pk
        self.fields['content_type'].initial = ContentType.objects.get_for_model(model).pk
        self.fields['goto'].initial = request.path
        # todo: Sign user,object_id,content_type values for security
        return self
