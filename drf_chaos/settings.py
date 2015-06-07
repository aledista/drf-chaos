"""
Settings for drf-chaos

DRF_CHAOS_ENABLED = True
"""
from django.conf import settings

DRF_CHAOS_ENABLED = getattr(settings, 'DRF_CHAOS_ENABLED', True)
