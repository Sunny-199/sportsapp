# from django.conf.urls import url
# from django.urls import path
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
# from chat.consumers import ChatConsumer
#
# application = ProtocolTypeRouter({
#     'websocket': AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 [
#                     path(r"^messages/(?P<chat_room>[\w.@+-]+)/$", ChatConsumer),
#
#                 ]
#             )
#         )
#     )
# })



import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
import chat.routing

from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            # path('messages/', ChatConsumer),
            chat.routing.websocket_urlpatterns
        )
    ),
})
