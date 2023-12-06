import ply.yacc as yacc
import ast
from Analizador_Lexico import tokens  # Import tokens from your lexical analyzer
from Analizador_Lexico import comando

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
    position : POSICION NUMERO NUMERO
    '''
    p[0] = (p[1], p[2], p[3])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Define the code to parse
code = comando

# Parse the code and generate the syntax tree
tree = ast.parse(code)

# Print the syntax tree
print(ast.dump(tree))