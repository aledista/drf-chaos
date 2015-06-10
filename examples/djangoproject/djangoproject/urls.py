from django.conf.urls import patterns, url

from .views import (
   ChaosApiView,
   DelayApiView,
   ErrorApiView,
   TestApiView,
   MimeTypeApiView,
)


urlpatterns = patterns('',
   url(r'^$', TestApiView.as_view(), name='api_test'),
   url(r'chaos$', ChaosApiView.as_view(), name='api_chaos'),
   url(r'delay', DelayApiView.as_view(), name='api_delay'),
   url(r'error$', ErrorApiView.as_view(), name='api_error'),
   url(r'mime_type', MimeTypeApiView.as_view(), name='api_mime_type'),
)
