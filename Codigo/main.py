from Laberinto import Laberinto 
import random
a=random.randint(5, 20)
b=random.randint(5, 20)
Prueba=Laberinto(width=a,height=b)
Prueba.generar_Laberinto()
Prueba.print_Laberinto()
