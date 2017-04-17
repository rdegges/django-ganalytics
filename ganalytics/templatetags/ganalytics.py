"""A simple Django templatetag that renders Google Analytics asynchronous
Javascript code.
"""

from django.conf import settings
from django import template
from django.template import Context
from django.template.loader import get_template


register = template.Library()


@register.simple_tag
def ganalytics():
    """Render Google Analytics tracking code if, and only if, the user has
    defined a ``GANALYTICS_TRACKING_CODE`` setting.
    """
    if (not settings.DEBUG) and getattr(settings, 'GANALYTICS_TRACKING_CODE', False):
        context = {'GANALYTICS_TRACKING_CODE': settings.GANALYTICS_TRACKING_CODE}
        return get_template('ganalytics/ganalytics.js').render(context)
    return ''
