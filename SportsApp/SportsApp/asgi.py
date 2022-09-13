"""
ASGI config for SportsApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

# import os
# import django
#
# from django.core.asgi import get_asgi_application
# from channels.routing import get_default_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SportsApp.settings')
# django.setup()
# application = get_asgi_application()
# application = get_default_application()


# import os
# import django
# from channels.routing import get_asgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SportsApp.settings")
# django.setup()
# application = get_asgi_application()

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SportsApp.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})