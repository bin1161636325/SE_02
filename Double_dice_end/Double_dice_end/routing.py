from django.urls import re_path

from api import consumers
from api import ready

websocket_urlpatterns = [
    # xxxxx/room/x1
    re_path(r'room/123/', consumers.ChatConsumer.as_asgi()),
    re_path(r'room/ready/', ready.Waiting.as_asgi()),
]