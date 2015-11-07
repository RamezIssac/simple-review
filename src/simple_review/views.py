import simplejson as json
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import RequestContext
from .forms import SimpleReviewForm


def get_review_form(request, model, **kwargs):
    return SimpleReviewForm(**kwargs).patch_form(request, model)


def post_review(request):
    if request.method == 'POST':
        next_url = request.POST.get('goto')
        form = SimpleReviewForm(request.POST)
        if form.is_valid():
            form.save()
            c = RequestContext(request, {
                'form': form,
                'object': form.instance
            })
            return_data = {'status':'ok', 'next':next_url}
        else:
            return_data = {'status':'fail', 'errors': form.errors}
        return HttpResponse(json.dumps(return_data), content_type='json')
    return HttpResponseNotAllowed('POST')
