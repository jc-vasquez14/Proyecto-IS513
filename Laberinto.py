import random

class Laberinto:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [['1' for x in range(width)] for y in range(height)]

    def generar_Laberinto(self):
      
        # Create a stack to hold the cell locations
        stack = []
        # Choose a random starting point
                
        start_x, start_y = random.randint(0, self.width-1), random.randint(0, self.height-1)
        self.maze[start_y][start_x] = 'X'
        # Add the starting point to the stack
        stack.append((start_x, start_y))

        while len(stack) > 0:
            x, y = stack[-1]
            # Find all neighbors of the current cell with 2 adjacent walls
            neighbors = [(x-2, y), (x+2, y), (x, y-2), (x, y+2)]
            neighbors = [(nx, ny) for nx, ny in neighbors if nx >= 0 and ny >= 0 and nx < self.width and ny < self.height and self.maze[ny][nx] == '1']
            if len(neighbors) == 0:
                # If the current cell has no neighbors, pop it from the stack
                stack.pop()
            else:
                # Choose a random neighbor
                nx, ny = random.choice(neighbors)
                # Remove the wall between the current cell and chosen cell
                self.maze[ny][nx] = '0'
                self.maze[y + (ny-y)//2][x + (nx-x)//2] = '0'
                # Push the chosen cell into the stack
                stack.append((nx, ny))

            # Set the bottom right cell as the final point
            self.maze[self.height-1][self.width-1] = '2'

        #Correcion de laberintos imposibles
        if self.maze[self.height-1][self.width-2] == '1' and self.maze[self.height-2][self.width-1] == '1':
            self.maze[self.height-2][self.width-1] = '0'
            self.maze[self.height-1][self.width-2] = '0'
    
        


    def borrar_Laberinto(self):
        self.maze= [['1' for x in range(self.width)] for y in range(self.height)]
                     
                    
            

    def check_maze(maze):
        # Find the starting point
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 'X':
                    start = (i, j)
                    break

        # Create a queue to hold the cell locations
        queue = []
        # Add the starting point to the queue
        queue.append(start)

        while len(queue) > 0:
            x, y = queue.pop(0)
            # Check if we have reached the end of the maze
            if maze[x][y] == '2':
                return True
            # Mark the current cell as visited
            maze[x][y] = 'V'
            # Find all neighbors of the current cell
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            # Add the unvisited neighbors to the queue
            for nx, ny in neighbors:
                if nx >= 0 and ny >= 0 and nx < len(maze) and ny < len(maze[0]) and maze[nx][ny] != 'V' and maze[nx][ny] != '1':
                    queue.append((nx, ny))

        # If we have exhausted all possible paths and haven't reached the end, the maze is unsolvable
        return False

    def print_Laberinto(self):
        for row in self.maze:
            print(' '.join(row))
