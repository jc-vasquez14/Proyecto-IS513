# Lenguajes de Programacion IS513

Reglas para Instrucciones
Cada instruccion o comando tiene que ser separado con una coma.En el caso de que se este
trabajando en un archivo .txt cada salto de linea tiene que ir al final con una coma.

Ejemplo:
-arriba,arriba,derecha,izquierda,pocision
+Eso es valido

arriba,arriba,derecha
izquierda
+Es invalido en el caso correcto deberia de ser
arriba,arriba,derecha,
izquierda

Reglas para Comentarios
El comentario tiene que ir despues de una instruccion 
Ejemplo:
-arriba,arriba (Comentario_Hola_Mundo),derecha
+Esto es valido

-arriba,(Comentario Hola Mundo) arriba 
+Esto no es valido

-arriba,(Comentario) arriba 
+Esto no es valido
