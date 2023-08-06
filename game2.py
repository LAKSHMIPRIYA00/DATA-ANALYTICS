# run this in terminal -> pip install pgzero 
import pgzrun
from random import randint
WIDTH = 1000
HEIGHT = 800
SCORE= 0

                   
def draw():
    screen.fill("white")                                                                                                         
    screen.draw.text(
        f"Score:{SCORE}",
        color="black",
        topleft=(10,10),
        fontsize=30
    )
    
def update(dt):
    print(dt)
pgzrun.go()
