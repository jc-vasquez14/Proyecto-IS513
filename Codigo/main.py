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



#Generacion del Laberinto
Lab=Laberinto(width=10,height=10)
Lab.generar_Laberinto()
Lab.print_Laberinto()
while True:

    code = input()


    # Genera el Arbol Sintactico
    tree = ast.parse(code)

    analizador.input(code)

    #limpiar_consola()

    for token in analizador:

       
        
        #print(f'Tipo: {token.type}, Valor: {token.value}')
        
        if token.value!=",":
            print(f'Tipo: {token.type}, Valor: {token.value}')
            Lab.movimientos(token.value)
            Lab.print_Laberinto()
            print("")
        

            
            



'''
Imprime el Arbol Sintactico
print(ast.dump(tree))

'''
