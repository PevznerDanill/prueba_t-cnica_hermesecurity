# Cómo maneja Django las vistas asíncronas?


En sus últimas actualizaciones los desarrolladores de Django han ido implementando cada vez más funcionalidades para garantizar la asincronía en el código. 

A partir de la versión 3 las vistas pueden ser declaradas como asíncronas (por ejemplo haciendo funciones async). Esto tiene sentido si la aplicación está desplegada en un servidor ASGI, sucesor asíncrono de WSGI.

El problema radica en el ORM de Django, que es síncrono, aunque los desarrolladores están trabajando para hacerlo asíncrono.

En la versión 5 de Django ya han aparecido algunas herramientas que permiten realizar cierta interacción con las bases de datos de manera asíncrona, por ejemplo usando métodos asave() o acreate(). Pero las transaciones siguen síncronas y para implementarlas en una vista asíncrona declarada con async hay que recurrir al método async_to_sync.

Además, existen librerías que permiten dotar de asincronía a las vistas de Django de otras maneras. 

Así, Django Channels, que también funcionan con ASGI, permiten utilizar código asíncrono y asíncrono. En este caso en vez de vistas podemos usar Consumers, que a su vez abren la posibilidad de manejar WebSockets (como en el caso de WebsocketConsumer).

Otra opción es usar Celery que permite crear una cola de tareas que se ejecutarán dentro de su propio bucle. Dentro de una vista de Django normal se puede añadir una tarea de Celery, iniciarla y en las próximas líneas del código devolver la respuesta HTTP, sin provocar timeout. En otras palabras, mientras una parte de nuestro código se está ejecutando, el resto sigue funcionando y el programa continúa funcionando, lo que supone asincronía.

