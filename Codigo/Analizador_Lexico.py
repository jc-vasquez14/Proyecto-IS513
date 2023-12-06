import ply.lex as lex
import re

contiene_error=False
# Definir los tokens
tokens = ['ARRIBA','ABAJO','IZQUIERDA','DERECHA','LIBRE','BLOQUEADO','TERMINAR','POSICION','NUMERO',"COMA"]

# Expresiones regulares para los tokens
t_ARRIBA = r'arriba'
t_ABAJO = r'abajo'
t_IZQUIERDA = r'izquierda'
t_DERECHA = r'derecha'
t_LIBRE = r'libre'
t_BLOQUEADO = r'bloqueado'
t_TERMINAR = r'terminar'
t_POSICION = r'pocision'
t_NUMERO = r'0|[1-9][0-9]'
t_COMA = r','

# Variable para contabilizar la aparición de "pocision"
pocision_count = 0

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'


    
# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Manejo de errores
def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)
    
    

# Expresión regular para comentarios
def t_COMMENT(t):
    r'\(.*?\)'
    pass





#Ejemplo del Analizador Lexico
analizador = lex.lex()

#Cadena de entrada a analizar
with open('comando.txt', 'r') as archivo:
    comando = archivo.read()

#Pasamos la cadena al analizador léxico
analizador.input(comando)
#Iteramos sobre los tokens generados e imprimimos su tipo y valor






