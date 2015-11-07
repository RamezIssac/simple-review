# simple-review
A Django extension for review feedback that use jQuery.raty. Batteries included.

# Installation

    pip install -e git+git@github.com:RamezIssac/simple-review.git@master#egg=django-simple-review
    python manage.py migrate

    Add 'simple_review' in `INSTALLED_APPS`

    Add `url(r'^post_review/$', post_review, name='post_review'),` to your urls.py

# Usage

In any page that you enable reviews:
1- Add review_form to context_data, so that it's rendered in the page

    from simple_review.views import get_review_form

    # Add the review form to context_data

    def get_context_data(self, **kwargs):
        context = super(InfoDetail, self).get_context_data(**kwargs)
        context['review_form'] = get_review_form(self.request, self.object)
        return context

2- Print the review form in the template. (remember, jQuery must be available on the page)
    {% include 'simple_review/review_form.html' %}


Review the test_app for a practical implementation and tests
