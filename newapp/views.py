import logging

from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render

logger = logging.getLogger('django.newapp')

# Create your views here.
def index(request):
    logger.warning(f'MODEL_SETTINGS_DICT: {settings.MODEL_SETTINGS_DICT}')
    logger.warning(f'DICT: {settings.DICT}')
    return JsonResponse({
        'MODEL_SETTINGS_DICT': settings.MODEL_SETTINGS_DICT,
        'DICT': settings.DICT,
    })

