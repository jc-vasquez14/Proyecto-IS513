import random
import sys
class Laberinto:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [['1' for x in range(width)] for y in range(height)]

    def generar_Laberinto(self):
      
        #Crear una pila para guardar la pocision de las celdas
        stack = []

        # Elgir un punto de partida aleatorio
        start_x, start_y = random.randint(0, self.width-1), random.randint(0, self.height-1)
        self.maze[start_y][start_x] = 'X'

        # Agregar el punto de partida X a la pila
        stack.append((start_x, start_y))

        while len(stack) > 0:
            x, y = stack[-1]

            # Encuentra todos los vecinos de la celda actual con 2 paredes adyacentes
            neighbors = [(x-2, y), (x+2, y), (x, y-2), (x, y+2)]
            neighbors = [(nx, ny) for nx, ny in neighbors if nx >= 0 and ny >= 0 and nx < self.width and ny < self.height and self.maze[ny][nx] == '1']
            
            if len(neighbors) == 0:
                #Si la celula actual no tiene vecines,le hacemos pop
                stack.pop()
            else:
                #Escoger un vecino aleatorio
                nx, ny = random.choice(neighbors)

                #Remover el muro entre la celula actual y la elegida
                self.maze[ny][nx] = '0'
                self.maze[y + (ny-y)//2][x + (nx-x)//2] = '0'

                #Push a la celula elegida en el stack
                stack.append((nx, ny))

            #Poner la celula abajo a la derecha como meta final.
            self.maze[self.height-1][self.width-1] = '2'

        #Correcion de laberintos imposibles
        if self.maze[self.height-1][self.width-2] == '1' and self.maze[self.height-2][self.width-1] == '1':
            self.maze[self.height-2][self.width-1] = '0'
            self.maze[self.height-1][self.width-2] = '0'
    
        

    def borrar_Laberinto(self):
        self.maze= [['1' for x in range(self.width)] for y in range(self.height)]
                     
                    
            

    def print_Laberinto(self):
        for row in self.maze:
            print(' '.join(row))

    
    def movimientos(self, comando):
        # Buscar la posición de la X en el laberinto
        for i in range(self.height):
            for j in range(self.width):
                if self.maze[i][j] == 'X':
                    x, y = i, j
                    break
        # Determinar la nueva posición según el comando
        if comando == "arriba":
            nx, ny = x - 1, y
        elif comando == "izquierda":
            nx, ny = x, y - 1
        elif comando == "derecha":
            nx, ny = x, y + 1
        elif comando == "abajo":
            nx, ny = x + 1, y
        elif comando == ",":
            nx, ny = x , y
        elif comando=="pocision":
            print('({},{})'.format(x, y))
            return
        elif comando=="terminar":
            sys.exit()
        else:
            print("Comando inválido")
            return
        
        # Verificar si la nueva posición es válida (no es una pared ni está fuera del laberinto)
        if nx >= 0 and ny >= 0 and nx < self.height and ny < self.width and self.maze[nx][ny] != '1':
            # Mover la X a la nueva posición y dejar un espacio vacío en la anterior
            self.maze[x][y] = '0'
            self.maze[nx][ny] = 'X'
            if self.maze[nx][ny]=='2':
                print("Meta")
               
            else:
                print("Libre")
        else:
            print("Bloqueado")
            
            


