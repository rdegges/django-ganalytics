"""A simple Django templatetag that renders Google Analytics asynchronous
Javascript code.
"""

from django.conf import settings
from django import template
from django.template import Context
from django.template.loader import get_template


register = template.Library()


@register.simple_tag
def google_analytics():
    """Render Google Analytics tracking code if, and only if, the user has
    defined a ``GOOGLE_ANALYTICS_TRACKING_CODE`` setting.
    """
    if hasattr(settings, 'GOOGLE_ANALYTICS_TRACKING_CODE') and settings.GOOGLE_ANALYTICS_TRACKING_CODE:
        context = Context({'GOOGLE_ANALYTICS_TRACKING_CODE': settings.GOOGLE_ANALYTICS_TRACKING_CODE})
        return get_template('google_analytics.js').render(context)
