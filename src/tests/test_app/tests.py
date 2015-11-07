from django.test import TestCase
from django.utils import translation
from simple_review.widgets import RateFieldWidget
from simple_review.models import Review


class TestRateField(TestCase):
    def test_correct_widget(self):
        rate_field = Review._meta.get_field_by_name('rate')[0]
        self.assertEqual(rate_field.formfield().widget.__class__, RateFieldWidget)


class TestRateWidget(TestCase):
    def test_media_dynamic_RTL(self):
        translation.activate('ar')
        w = RateFieldWidget()
        self.assertTrue('raty.rtl.css' in w.media.render())

    def test_render(self):
        w = RateFieldWidget()
        render_results = w.render('dummy_name', '4.5')
        self.assertIn('scoreName="dummy_name"', render_results)
        self.assertIn('data-score="4.5"', render_results)

    def test_defaults_implementation(self):
        w = RateFieldWidget()
        render_results = w.render('dummy_name', '4.5')
        self.assertIn(' $.extend($.fn.raty.defaults,', render_results)


class TestForm(TestCase):
    def test_patch_form(self):
        # todo
        pass


class TestTemplates(TestCase):
    # todo
    pass
