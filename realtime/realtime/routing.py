from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddleware

from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    'websocket': AuthMiddleware(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
