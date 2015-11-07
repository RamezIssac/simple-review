from django.views.generic import DetailView
from .models import Information
from simple_review.views import get_review_form


class InfoDetail(DetailView):
    model = Information
    template_name = 'review_form.html'

    def get_context_data(self, **kwargs):
        context = super(InfoDetail, self).get_context_data(**kwargs)
        context['review_form'] = get_review_form(self.request, self.object)
        context['reviews'] = self.object.reviews.all()

        return context
