from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_chaos.decorators import (
    chaos,
    delay,
    error,
)


class TestApiView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChaosApiView(APIView):
    @chaos(rate=0.5)
    def get(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)


class DelayApiView(APIView):
    @delay(rate=0.5, milliseconds=700)
    def get(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)


class ErrorApiView(APIView):
    @error(rate=0.5, status=500)
    def get(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)
