#Libraries
import wave
import sys
import pyaudio
import pygame
import recordAudio as ra


#Setting up the Game
pygame.init
screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
pygame.display.set_caption('Mic Checkers')
bg = pygame.image.load('./images/miccheck_bg.png')
icon = pygame.image.load('./images/miccheck_icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

buttonSizeScale = (80, 80)
redplaybutton = pygame.transform.scale(pygame.image.load("images/redplay.png"), buttonSizeScale)
greenplaybutton = pygame.transform.scale(pygame.image.load("images/greenplay.png"), buttonSizeScale)


#Setting up Global Variables
leaveScreen = False
running = True
color = (245, 245, 220)


def game_intro():
    global running
    global leaveScreen

    while running and not leaveScreen:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
            elif keys[pygame.K_RETURN]:
                leaveScreen = True
    
        #Rendering new things onto screen
        screen.fill('white')

        #Updating displaying the new screen
        pygame.display.update()
        clock.tick(60)


def game_recording():
    global running
    global leaveScreen

    leaveScreen = False
    while running and not leaveScreen:
        #Poll for events
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
            # elif keys[pygame.K_RETURN]:
            #     leaveScreen = True
            elif keys[pygame.K_SPACE]:
                #code
                ra.record()

        

        #Rendering new things onto screen
        screen.fill(color)
            #screen.blit //puts images onto screen
        playSoundButton(100, 100, 100, 100, redplaybutton, "sounds/dog/dog1.wav")
        #Updating displaying the new screen
        pygame.display.update()
        clock.tick(60)

def playSoundButton(x, y, w, h, img, soundFile):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, w, h)
    on_button = rect.collidepoint(mouse)

    screen.blit(img, img.get_rect(center = rect.center))

    if on_button:
        if click[0] == 1:
            ra.playAudio(soundFile)


game_intro()
game_recording()
#game_guessing()
    #should we display the correct answer?
    #way to go back to the intro screen?
pygame.quit()