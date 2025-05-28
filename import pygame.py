import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))
running = True
while(running):
    
    events = pygame.event.get()
    for e in events:
        if(e.type==pygame.QUIT):
            running = False

pygame.quit()