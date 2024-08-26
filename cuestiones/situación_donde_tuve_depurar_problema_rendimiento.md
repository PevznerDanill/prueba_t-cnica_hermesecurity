# Describe una situación en la que tuviste que depurar un problema de rendimiento en una aplicación Django. ¿Qué pasos tomaste para resolverlo?


En una aplicación de mensajería instantánea tuve que añadir una función 
para marcar todos los mensajes en todos los chats de un usuario como leídos. 

Pese a que la lógica parece sencilla – encontrar todos los chats y los mensajes asociados
al usuario y marcar el campo correspondiente (is_read) como True – el problema surgió cuando considiré
que un usuario puede tener centenares de chats con miles de mensajes cada uno. 

Así que hacerlo todo dentro de una simple vista POST podría suponer un error de timeout debido al volumen de los datos procesados. 

Para solucionar esto, implementé una tarea asíncrona utilizando Celery. 
Añadí la tarea de Celery para marcar los mensajes como leídos y, sin esperar a que se completara la tarea, 
devolví un HttpResponse 200. 

Esto permitió que la operación se ejecutara en segundo plano y así evité problemas de rendimiento y timeout.
Yo diría que cuando necesito que se ejecute un código que puede tardar mucho y al mismo tiempo quiero 
que el resto de la aplicación continúe funcionando sin interrupciones. 
