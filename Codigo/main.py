import ast
from Analizador_Lexico import tokens,analizador
from Analizador_Sintactico import parser
import ply.yacc as yacc

# Suponiendo que 'tree' es el árbol de sintaxis generado por ast.parse()
def translate_directions(node):
    if isinstance(node, ast.Expr):
        translate_directions(node.value)
    elif isinstance(node, ast.Call):
        translate_directions(node.func)
        for arg in node.args:
            translate_directions(arg)
    elif isinstance(node, ast.Name):
        direction_mapping = {
            'arriba': 'W',
            'abajo': 'S',
            'izquierda': 'A',
            'derecha': 'D'
        }
        if node.id in direction_mapping:
            print(f"Traducción: {direction_mapping[node.id]}")
        else:
            print(f"No se encontró una traducción para '{node.id}'")
    else:
        print(f"Tipo de nodo no compatible: {type(node)}")



#Cadena de entrada a analizar
with open('comando.txt', 'r') as archivo:
    comando = archivo.read()


# Define the code to parse
code = comando

# Parse the code and generate the syntax tree
tree = ast.parse(code)



for token in analizador:
    print(f'Tipo: {token.type}, Valor: {token.value}')
    


print(ast.dump(tree))


analizador.input(code)

direction_mapping = {
    'arriba': 'W',
    'abajo': 'S',
    'izquierda': 'A',
    'derecha': 'D'
}

# Lista para almacenar las direcciones traducidas
translated_directions = []


for token in analizador:
    if token.value in direction_mapping:
        translated_directions.append(direction_mapping[token.value])

# Imprimir el resultado
print("Direcciones traducidas:", translated_directions)
