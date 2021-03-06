import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racing car")
clock = pygame.time.Clock()

carImg = pygame.image.load("racecar1.png")
car_width = 230


def things(thing_x, thing_y, thing_w, thing_h, color):
    pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_w, thing_h])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def textobjects(mesg, largeText):
    textsurf = largeText.render(mesg, True, red, white)
    return textsurf, textsurf.get_rect()


def message_display(mesg):
    largeText = pygame.font.Font('freesansbold.ttf', 32)
    textSurf, textRect = textobjects(mesg, largeText)
    textRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)


def crash():
    message_display("You Crashed")


def game_loop():
    x_change = 0

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 50
    thing_height = 50
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_LEFT:
                    x_change = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x, y)

        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
