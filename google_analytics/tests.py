from django.conf import settings
from django.template import Context, Template, TemplateSyntaxError
from django.test import TestCase


class GoogleAnalytics(TestCase):

    def setUp(self):
        self.orig = settings.GOOGLE_ANALYTICS_TRACKING_CODE
        self.render = lambda t: Template(t).render(Context())

    def test_can_load_google_analytics_template_tags(self):
        self.assertEqual(self.render('{% load google_analytics %}'), '')

    def test_render_fails_without_including_template_tag(self):
        self.assertRaises(TemplateSyntaxError, self.render, '{% google_analytics %}')

    def test_render_doesnt_render_anything_if_no_setting_exists(self):
        del settings.GOOGLE_ANALYTICS_TRACKING_CODE
        self.assertEqual(self.render('{% load google_analytics %}{% google_analytics %}'), '')

    def test_render_doesnt_render_anything_if_the_setting_exists_but_is_not_valid(self):
        settings.GOOGLE_ANALYTICS_TRACKING_CODE = ''
        self.assertEqual(self.render('{% load google_analytics %}{% google_analytics %}'), '')

        settings.GOOGLE_ANALYTICS_TRACKING_CODE = None
        self.assertEqual(self.render('{% load google_analytics %}{% google_analytics %}'), '')

    def test_render_returns_javascript_code_if_setting_exists(self):
        self.assertIn('UA-12345678-90', self.render('{% load google_analytics %}{% google_analytics %}'))

    def tearDown(self):
        settings.GOOGLE_ANALYTICS_TRACKING_CODE = self.orig
