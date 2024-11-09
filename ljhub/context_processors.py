# ljhub/context_processors.py
from django.conf import settings


def support_email(request):
    return {
        'support_email': settings.SUPPORT_EMAIL
    }
