import wave
import sys
import pyaudio
import pygame
import recordAudio as ra

#Setting up Game
pygame.init
pygame.display.set_caption('Mic Checkers')
screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)

clock = pygame.time.Clock()
running = True
keys = pygame.key.get_pressed()

#Setting Variables
color = (245, 245, 220)
bg = pygame.image.load('./images/miccheck_bg.png')
icon = pygame.image.load('./images/miccheck_icon.png')
pygame.display.set_icon(icon)
green = (0, 255, 0)

def game_intro():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
            elif keys[pygame.K_RETURN]:
                print('hello :3')
    
    #Rendering new things onto screen
    screen.fill(green)

    #Updating displaying the new screen
    pygame.display.update()
    clock.tick(60)


def game_main():
    running = True
    while running:
        #poll for events
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
            elif keys[pygame.K_SPACE]:
                #code
                ra.record()

        #remove frames
        screen.fill(color)
        #screen.blit //puts something like text or images onto screen

        #render game
        #pygame.display.flip() #displays screen
        pygame.display.update()
        clock.tick(60)

game_intro()
game_main()
pygame.quit()