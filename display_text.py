import pygame
pygame.init()
import time

clock = pygame.time.Clock()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racing car")

carImg = pygame.image.load("racecar1.png")
car_width = 230

white = (255,255, 255)
black = (0,0,0)
red = (255, 0,0)

def car(x, y):
    gameDisplay.blit(carImg, (x,y))

def textobjects(mesg, largeText):
    textsurf = largeText.render(mesg, True, red , white)
    return textsurf, textsurf.get_rect()

def message_display(mesg):
    largeText = pygame.font.Font('freesansbold.ttf', 32)
    textSurf, textRect = textobjects(mesg, largeText)
    textRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)


def crash():
    message_display("You Crashed")

def game_loop():
    x_change = 0

    x = display_width * 0.45
    y = display_height * 0.1

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
        car(x, y)

        if x > display_width - car_width or x < 0:
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
