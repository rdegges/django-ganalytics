"""A simple Django templatetag that renders Google Analytics asynchronous
Javascript code.
"""

from django.conf import settings
from django import template
from django.template import Context
from django.template.loader import get_template


register = template.Library()


@register.simple_tag(takes_context=True)
def ganalytics(context):
    """Render Google Analytics tracking code if, and only if, the user has
    defined a ``GANALYTICS_TRACKING_CODE`` setting.
    """
    if (not settings.DEBUG) and getattr(settings, 'GANALYTICS_TRACKING_CODE', False):
        render_context = {'GANALYTICS_TRACKING_CODE': settings.GANALYTICS_TRACKING_CODE}
        if getattr(settings, 'GANALYTICS_TRACK_USERS', False):
            user = context['user']
            render_context['USER_ID'] = user.id if user.is_authenticated() else None
        return get_template('ganalytics/ganalytics.js').render(render_context)
    return ''
