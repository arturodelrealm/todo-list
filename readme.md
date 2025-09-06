# Todo list

Url: https://todo-list-st.fly.dev/

Desarrollada completamente con el modelo MVC de Django.

**Uso de IA:** 

Se usó Chatgpt como ayuda para generar código más rápidamente, en particular le pedí:

* Una base de la app con las vistas del CRUD de las Task en base al modelo dado.
* Mejorar los templates entregados por defecto, usando bootstrap.
* Ajustes de algunas observaciones en los templates, por ejemplo, pedir que se genere un modal 
 de confirmación o usar datatables para la lista de tareas.
* Ayudas con funcionalidades específicas, como por ejemplo el como hacer el mock de un test.
* Creación de una base para tests de las vistas.

Se validó usando la aplicación y revisando el código. Se hizo una revisión linea por linea del código en Python, 
pero una más general en el HTML.

En muchos casos la IA cometía errores pequeños que eran solucionados o al probarlo o en la revisión manual.

**Decisiones relevantes:**

* Se generó una interfaz para la generación de la estimación de tiempo, para facilitar la creación o modificación de 
 estas.
* Se generó un servicio de tareas que ayuda a obtener los permisos de un usuario sobre las tareas, evitando el 
 `select * from tasks` directo. Esto facilitará en el futuro hacer cambios sobre los permisos, por ejemplo hacer que
 un usuario pueda ver solo sus tareas, o un admin pueda ver todo.
* Se usó HuggingFace por simplicidad y gratuidad. No valía la pena servir un modelo propio local (aunque sea sencillo), 
 dado que se usan máquinas pequeñas para el deploy. Haciendo una breve investigación se llegó al modelo de HuggingFace, 
 en caso de que sea necesario modificarlo en el futuro sería sencillo con el uso de la interfaz.
* Por simplicidad y mi poca experiencia en fron-end se hizo el desarrollo como MVC, aunque dada la naturaleza del 
proyecto, parece ser la opción más natural.


**Tiempo de desarrollo**

En total el desarrollo me tomó unas 8 horas (más de las 4 horas que estimaba en un principio).

Partí creando un servicio de LLM, cosa que me tomó casi 2 horas.

Luego la creación de la aplicación me tomó unas 5 horas, entre ir agregando funcionalidades mínimas (completar 
descompletar por ejemplo), e ir mejorando la interfaz.

1 Hora subiendo la aplicación a fly io y hacer una revisión de que todo este en orden.
