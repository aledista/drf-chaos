import time
from random import random, randint

from django.http import HttpResponse

from .settings import DRF_CHAOS_ENABLED


class ChaosMiddleware(object):
    def process_response(self, request, response):
        if random() >= 0.5 and DRF_CHAOS_ENABLED:
            time.sleep(randint(0, 3))
            response = HttpResponse()
            response.status_code = randint(300, 599)
        else:
            return response
