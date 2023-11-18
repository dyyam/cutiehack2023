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
pygame.font.init()

buttonSizeScale = (80, 80)
redplaybutton = pygame.transform.scale(pygame.image.load("images/redplay.png"), buttonSizeScale)
greenplaybutton = pygame.transform.scale(pygame.image.load("images/greenplay.png"), buttonSizeScale)
title_playbutton = pygame.image.load("./images/play_button.png")

#Setting up Global Variables
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
leaveScreen = False
running = True
color = (245, 245, 220)


def title_screen():
    #FIxme: title screen not centering
    global running
    global leaveScreen

    #Setting the Text Size, Font, and Placement
    title_font = pygame.font.SysFont('Comic Sans MS', 80)
    title = title_font.render('Mic Check', True, (0, 0, 0))
    title_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 20))

    subtitle_font = pygame.font.SysFont('Comic Sans MS', 20)
    subtitle = subtitle_font.render('By: David Yam + Vincent Vo', True, (0,0,0))
    subtitle_rect = title.get_rect(center=(SCREEN_WIDTH/2 + 60, SCREEN_HEIGHT/2 + 120))

    icon = pygame.transform.scale(pygame.image.load("images/miccheck_icon.png"), (350, 300))

    while running and not leaveScreen:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
            elif keys[pygame.K_RETURN]:
                leaveScreen = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if checkButtonPress(SCREEN_WIDTH/2 + 50, SCREEN_HEIGHT/2 + 160, 100, 100):
                    leaveScreen = True
    
        #Rendering new things onto screen
        print(str(title_playbutton.get_width))
        print(str(title_playbutton.get_height))
        screen.fill((172,229,238))
        screen.blit(icon, icon.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 200)))
        screen.blit(title, title_rect)
        screen.blit(subtitle, subtitle_rect)
        screen.blit(title_playbutton, title.get_rect(center=(SCREEN_WIDTH/2 + 50, SCREEN_HEIGHT/2 + 160)))

        #Updating displaying the new screen
        pygame.display.update()
        clock.tick(60)


def recording_screen():
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

def checkButtonPress(x, y, w, h):
    rect = pygame.Rect(x, y)
    mouse = pygame.mouse.get_pos()


    result = rect.collidepoint(mouse)
    if result:
        print('hehe')

    #return bool




title_screen()
    #moving title text?
    #play button changes color?
recording_screen()
#guessing_screen()
#end_screen()
    #way to navigate back to title screen
pygame.quit()