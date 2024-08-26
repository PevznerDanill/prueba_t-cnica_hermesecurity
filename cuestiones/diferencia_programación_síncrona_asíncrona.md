# Explica la diferencia entre programación síncrona y asíncrona


En la programación síncrona el código se ejecuta línea por línea. 
El programa no va a comenzar a ejecutar la siguiente línea de código hasta que haya terminado con la línea anterior. 
Así se garantiza el orden de ejecución del código en un programa, pero a veces puede resultar en un mayor tiempo de implementación.


En la programación asíncrona las nuevas líneas de código pueden comenzar a ejecutarse 
sin esperar a que finalice la ejecución del código anterior, ya que éste se maneja a través de un bucle de eventos. 

Es decir, podemos iniciar una tarea, y mientras que el código correspondiente se está ejecutando
podemos comenzar a ejecutar un nuevo código.

Esto puede alterar el órden de ejecución, pero acelera el programa y, 
lo que a mí me parece lo crucial, garantiza que el programa continúe funcionando sin interrupciones.