from django.conf import settings
from django.template import Context, Template, TemplateSyntaxError
from django.test import TestCase


class GoogleAnalytics(TestCase):

    def setUp(self):
        self.orig = settings.GANALYTICS_TRACKING_CODE
        self.render = lambda t: Template(t).render(Context())

    def test_can_load_google_analytics_template_tags(self):
        self.assertEqual(self.render('{% load ganalytics %}'), '')

    def test_render_fails_without_including_template_tag(self):
        self.assertRaises(TemplateSyntaxError, self.render, '{% ganalytics %}')

    def test_render_doesnt_render_anything_if_no_setting_exists(self):
        del settings.GANALYTICS_TRACKING_CODE
        self.assertEqual(self.render('{% load ganalytics %}{% ganalytics %}'), '')

    def test_render_doesnt_render_anything_if_the_setting_exists_but_is_not_valid(self):
        settings.GANALYTICS_TRACKING_CODE = ''
        self.assertEqual(self.render('{% load ganalytics %}{% ganalytics %}'), '')

        settings.GANALYTICS_TRACKING_CODE = None
        self.assertEqual(self.render('{% load ganalytics %}{% ganalytics %}'), '')

    def test_render_returns_javascript_code_if_setting_exists(self):
        settings.GANALYTICS_TRACKING_CODE = 'UA-12345678-90'
        self.assertIn('UA-12345678-90', self.render('{% load ganalytics %}{% ganalytics %}'))

    def tearDown(self):
        settings.GANALYTICS_TRACKING_CODE = self.orig
