import ply.yacc as yacc
import ast
from Analizador_Lexico import tokens  #Importar token del analizador lexico


# Define the grammar rules
def p_command(p):
    '''
    command : movement
            | status
            | end
            | position
    '''

def p_command_list(p):
    '''
    command_list : command_list COMA command
                 | command
    '''

def p_movement(p):
    '''
    movement : ARRIBA
             | ABAJO
             | IZQUIERDA
             | DERECHA
    '''

def p_status(p):
    '''
    status : LIBRE
           | BLOQUEADO
    '''

def p_end(p):
    '''
    end : TERMINAR
    '''

def p_position(p):
    '''
    position : POSICION 
    '''
    p[0] = (p[1], p[2], p[3])

# Error para errores de sintaxis (syntax errors)
def p_error(p):
    print("SyntaxError!")


#Crear el analizadpr
parser = yacc.yacc()






# Build the parser
parser = yacc.yacc()

