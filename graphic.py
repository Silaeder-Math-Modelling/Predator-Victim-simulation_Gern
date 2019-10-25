import pygame
from random import randint
from animal_class import Predator, Victim

pygame.init()

pi = 3.14
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

size = [1100, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First (not)good version")

done = False
clock = pygame.time.Clock()

Fox = Predator(550, 300)

Rabbits = []
for i in range(0, 10):
	Rabbits.append(Victim(randint(0, 1100), randint(0, 300)))

while not done:
    clock.tick(10)

    pygame.draw.circle(screen, RED, 550, 300, 10, 0)
    Fox_coordinate = Fox.get_coordinates()

    for Rabbit in Rabbits:
    	Rabbit_coordinate = Rabbit.get_coordinates()
    	pygame.draw.circle(screen, GREEN, Rabbit_coordinate[0] - Fox_coordinate[0], Rabbit_coordinate[1] - Fox_coordinate[1], 5, 0)
    	Rabbit.update_coordinates()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(WHITE)
    Fox.update_coordinates()


pygame.quit()