# Cómo se puede integrar Django con websockets?


Como ya he dicho antes, se puede integrar Django con WebSockets a través de Django Channels y precisamente sus Consumers (WebsocketConsumer). 

Primero hay que instalar Django Channels y configurarlo para trabajar con un servidor ASGI. Dentro de Django Channels para manejar las conexiones de WebSocket se utilizan Consumers que por su lógica son similares a las vistas de Django, solo que no requieren devolver la respuesta HTTP (lo que es lógico, ya que no se trata de un protocolo petición-respuesta, sino de un canal abierto por el que los datos se transportan en dos direcciones de manera contínua).

La configuración de las rutas para los Consumers se realiza en un archivo routing.py. Allí se puede utilizar ProtocolTypeRouter para definir qué protocolo manejará cada tipo de conexión.

Aquí está un ejemplo de mi proyecto actual:

```python
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from authorization.jwt.channels_middleware_ws import TokenAuthMiddlewareStack
from consumers.alert import AlertConsumer
from consumers.chat import ChatConsumer

application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddlewareStack(
        URLRouter([
            path("ws/instance/<room>/", ChatConsumer),
            path("ws/alert/<user_id>/", AlertConsumer)
        ]),
    ),
})
```
 
Tanto ChatConsumer como AlertConsumer son subclases de WebsocketConsumer, que cuanta con métodos integrados como connect, disconnect close, recieve, send y otros, lo necesario para manejar las conexiónes WebSocket y lo que permite crear aplicaciones que funcionan en tiempo real, como chats, notificaciones en vivo, y todo esto integrado dentro de un proyecto de Django. 
