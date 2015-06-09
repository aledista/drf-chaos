import time
from random import random, randint, choice

from django.http import HttpResponse
from django.http.response import REASON_PHRASES

from .settings import DRF_CHAOS_ENABLED


class ChaosMiddleware(object):
    def process_response(self, request, response):
        if random() >= 0.5 and DRF_CHAOS_ENABLED:
            time.sleep(randint(0, 3))
            response = HttpResponse()
            status_code = choice(REASON_PHRASES.keys())
            response.status_code = status_code
            response.reason_phrase = REASON_PHRASES.get(
                status_code,
                'UNKNOWN STATUS CODE'
            )
            response.content = "drf-chaos: {}".format(
                response.reason_phrase
            )
        return response
