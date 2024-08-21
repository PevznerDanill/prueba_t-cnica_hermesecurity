from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/progress/$', consumers.ProgressBarConsumer.as_asgi()),
]
