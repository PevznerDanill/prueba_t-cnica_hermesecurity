# Qué es Django Channels y cómo habilita el soporte para WebSockets


Pues Django Channels es un proyecto extiende Django para manejar conexiones asíncronas de larga duración, como WebSockets o HTTP2 y protocolos de IoT.

Por defecto Django utiliza WSGI, que es síncrono y no admite conexiones persistentes como WebSockets. 

A su vez, Channels introduce su propio servidor ASGI, lo que permite que una aplicación Django pueda trabajar tanto con solitudes HTTP como conexiones WebSocket de manera asíncrona.