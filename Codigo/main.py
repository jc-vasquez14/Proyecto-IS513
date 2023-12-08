import ast
from Analizador_Lexico import tokens,analizador
from Analizador_Sintactico import parser
import ply.yacc as yacc
from Laberinto import *
import os
import sys

#Comando
def limpiar_consola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")




Lab=Laberinto(width=10,height=10)
Lab.generar_Laberinto()
Lab.print_Laberinto()

# Define the code to parse
code = input()


# Parse the code and generate the syntax tree
tree = ast.parse(code)

analizador.input(code)
limpiar_consola()

for token in analizador:

    Lab.movimientos(token.value)
    
    # print(f'Tipo: {token.type}, Valor: {token.value}')
    if token.value!=",":
        print(f'Tipo: {token.type}, Valor: {token.value}')
        Lab.print_Laberinto()
    


'''
print(ast.dump(tree))

'''
