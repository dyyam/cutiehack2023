import wave
import sys
import pyaudio

import pygame

pygame.init
screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
pygame.display.set_caption('Mic Checkers')
clock = pygame.time.Clock()
running = True

while running:
    #poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    #remove frames
    screen.fill('purple')

    #render game
    pygame.display.flip() #displays screen
    clock.tick(60)

pygame.quit()