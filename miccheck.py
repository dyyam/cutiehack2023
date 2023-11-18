import wave
import sys
import pyaudio
import pygame

#Setting up Game
pygame.init
screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
pygame.display.set_caption('Mic Checkers')
clock = pygame.time.Clock()
running = True

#Setting Variables
color = (245, 245, 220)
bg = pygame.image.load('./images/miccheck_bg.png')
icon = pygame.image.load('./images/miccheck_icon.png')

pygame.display.set_icon(icon)

while running:
    #poll for events
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    #remove frames
    screen.fill(color)

    #render game
    #pygame.display.flip() #displays screen
    pygame.display.update()
    clock.tick(60)

pygame.quit()