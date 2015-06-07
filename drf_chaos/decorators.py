import time
from random import random, randint

import wrapt
from rest_framework.response import Response


def chaos(rate):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        if random() >= rate:
            time.sleep(randint(0, 3))
            return Response(status=randint(300, 599))
        else:
            return wrapped(*args, **kwargs)

    return wrapper


def delay(rate, seconds):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        if random() <= rate:
            time.sleep(seconds)
        return wrapped(*args, **kwargs)

    return wrapper


def error(rate, status):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        if random() <= rate:
            return Response(status=status)
        else:
            return wrapped(*args, **kwargs)

    return wrapper



