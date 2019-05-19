import sys, pygame
from pygame.locals import *
pygame.init()

size = width, height = 500, 500

distance = [0,0]
speed = [10,0.5]
gravity = [0,0.5]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

ball = pygame.image.load("football.png")
ballrect = ball.get_rect()
pressed=0

BOUNCE=2
ROLL=1
STOP=0
state = BOUNCE


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = 1
        if event.type == pygame.MOUSEBUTTONUP:
            pressed = 0
    key = pygame.key.get_pressed()
    if key[K_ESCAPE]:
        pygame.QUIT: sys.exit()

    mouse = pygame.mouse.get_rel()
    if pressed:
        speed=[10,0.5]
        state = BOUNCE
        distance =[0,0]
        ballrect = ballrect.move(mouse)
    else:
        if state == BOUNCE:
            if speed[1] < 5 and speed[1] >-5 and ballrect.bottom > height - 5:
                state=ROLL
                distance[1]=0
        if state == ROLL:
            if speed[0] < 0.5 and speed[0] > -0.5:
                state=STOP


        if state == BOUNCE:
            speed[0] += gravity[0]
            speed[1] += gravity[1]
            
            distance[0] = speed[0]
            distance[1] = speed[1]

            if ballrect.left < 0 or ballrect.right > width:
                speed[0] = -speed[0]*0.9
                distance[0] = -distance[0]
            if ballrect.top < 0 or ballrect.bottom > height:
                speed[1] = -speed[1]*0.8
                distance[1] = -distance[1]
            ballrect = ballrect.move(distance)
    
        if state == ROLL:
            speed[0] = speed[0]*0.95
            distance[0] = speed[0]
            if ballrect.left < 0 or ballrect.right > width:
                speed[0] = -speed[0]
                distance[0] = -distance[0]
            ballrect = ballrect.move(distance)

    screen.fill(black)
    ## copy ball image to display area
    screen.blit(ball, ballrect)
    pygame.display.update()
