#Libraries
import wave
import sys
import pyaudio
import pygame
import recordAudio as ra
from time import sleep


#Setting up the Game
pygame.init
screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
pygame.display.set_caption('Mic Checkers')
bg = pygame.image.load('./images/miccheck_bg.png')
icon = pygame.image.load('./images/miccheck_icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
pygame.font.init()

buttonSizeScale = (50, 50)
redplaybutton = pygame.transform.scale(pygame.image.load("images/redplay.png"), buttonSizeScale)
greenplaybutton = pygame.transform.scale(pygame.image.load("images/greenplay.png"), buttonSizeScale)
title_playbutton = pygame.image.load("./images/play_button.png")
choice1 = pygame.transform.scale(pygame.image.load("images/choice1.png"), buttonSizeScale)
choice2 = pygame.transform.scale(pygame.image.load("images/choice2.png"), buttonSizeScale)
choice3 = pygame.transform.scale(pygame.image.load("images/choice3.png"), buttonSizeScale)
choice4 = pygame.transform.scale(pygame.image.load("images/choice4.png"), buttonSizeScale)
choice5 = pygame.transform.scale(pygame.image.load("images/choice5.png"), buttonSizeScale)
checkmark = pygame.transform.scale(pygame.image.load("images/checkmark.png"), buttonSizeScale)

speakingSizeScale = (150, 150)
notspeaking = pygame.transform.scale(pygame.image.load('./images/notspeaking.png'), speakingSizeScale)
speaking = pygame.transform.scale(pygame.image.load('./images/speaking.png'), speakingSizeScale)

submitSizeScale = (300, 100)
submitbutton = pygame.transform.scale(pygame.image.load('./images/submitbutton.png'), submitSizeScale)

#Setting up Global Variables
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
leaveScreen = False
running = True
color = (245, 245, 220)


def title_screen():
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
    
        #Rendering new things onto screen
        screen.fill((172,229,238))
        screen.blit(icon, icon.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 200)))
        screen.blit(title, title_rect)
        screen.blit(subtitle, subtitle_rect)
        submitButton(SCREEN_WIDTH/2.6, SCREEN_HEIGHT/1.4, submitSizeScale[0], submitSizeScale[1], title_playbutton)

        #Updating displaying the new screen
        pygame.display.update()
        clock.tick(60)


def recording_screen():
    title_font = pygame.font.SysFont('Comic Sans MS', 40)
    title = title_font.render('Try to mimic the prompt as best you can!', True, (0, 0, 0))
    title_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/16))

    prompt_font = pygame.font.SysFont('Comic Sans MS', 35)
    prompt = prompt_font.render('Your prompt is: Dog', True, (200, 0, 0))
    prompt_rect = prompt.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8))

    sample_font = pygame.font.SysFont('Comic Sans MS', 30)
    sample = sample_font.render('Sample sound', True, (0, 0, 0))
    sample_rect = sample.get_rect(center=(SCREEN_WIDTH/2.1, SCREEN_HEIGHT/5))

    instruct_font = pygame.font.SysFont('Comic Sans MS', 30)
    instruct = instruct_font.render('Hold SPACE to record!', True, (0, 0, 0))
    instruct_rect = instruct.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    
    global running
    global leaveScreen

    leaveScreen = False
    
    while running and not leaveScreen:
        #Poll for events
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
            elif keys[pygame.K_SPACE]:
                ra.record()
        


        #Rendering new things onto screen
        screen.fill(color)
            #screen.blit //puts images onto screen
        screen.blit(title, title_rect)
        screen.blit(prompt, prompt_rect)
        screen.blit(sample, sample_rect)
        screen.blit(instruct, instruct_rect)
        
        talkingHead()
        playSoundButton(SCREEN_WIDTH/1.8, SCREEN_HEIGHT/6, buttonSizeScale[0], buttonSizeScale[1], redplaybutton, "sounds/dog/dog1.wav")
        submitButton(SCREEN_WIDTH/2.6, SCREEN_HEIGHT/1.8, submitSizeScale[0], submitSizeScale[1], submitbutton)
        
        #Updating displaying the new screen
        pygame.display.update()
        clock.tick(60)


def guessing_screen():
    global running
    global leaveScreen
    global selected


    #Setting the Text Size, Font, and Placement
    title_font = pygame.font.SysFont('Comic Sans MS', 40)
    title = title_font.render('Which one is the imposter?', True, (0, 0, 0))
    title_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/16))

    prompt_font = pygame.font.SysFont('Comic Sans MS', 35)
    prompt = prompt_font.render('The prompt was: Dog', True, (0, 120, 0))
    prompt_rect = prompt.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8))

    leaveScreen = False

    selected = 0

    while running and not leaveScreen:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
    
        #Rendering new things onto screen
        screen.fill((211, 211, 222))
        screen.blit(title, title_rect)
        screen.blit(prompt, prompt_rect)

        choiceButton(SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/5, choice1, 1)
        choiceButton(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/5, choice2, 2, correct=True)
        choiceButton(SCREEN_WIDTH/2, SCREEN_HEIGHT/5, choice3, 3)
        choiceButton(SCREEN_WIDTH/2 + 100, SCREEN_HEIGHT/5, choice4, 4)
        choiceButton(SCREEN_WIDTH/2 + 200, SCREEN_HEIGHT/5, choice5, 5)

        playSoundButton(SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/3.5, buttonSizeScale[0], buttonSizeScale[1], greenplaybutton, "sounds/dog/dog1.wav")
        playSoundButton(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/3.5, buttonSizeScale[0], buttonSizeScale[1], greenplaybutton, "sounds/output.wav")
        playSoundButton(SCREEN_WIDTH/2, SCREEN_HEIGHT/3.5, buttonSizeScale[0], buttonSizeScale[1], greenplaybutton, "sounds/dog/dog2.wav")
        playSoundButton(SCREEN_WIDTH/2 + 100, SCREEN_HEIGHT/3.5, buttonSizeScale[0], buttonSizeScale[1], greenplaybutton, "sounds/dog/dog3.wav")
        playSoundButton(SCREEN_WIDTH/2 + 200, SCREEN_HEIGHT/3.5, buttonSizeScale[0], buttonSizeScale[1], greenplaybutton, "sounds/dog/dog4.wav")

        submitButton(SCREEN_WIDTH/2.6, SCREEN_HEIGHT/1.4, submitSizeScale[0], submitSizeScale[1], submitbutton)

        #Updating displaying the new screen
        pygame.display.update()
        clock.tick(60)


def end_screen():
    print('hello')


def playSoundButton(x, y, w, h, img, soundFile):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, w, h)
    on_button = rect.collidepoint(mouse)

    screen.blit(img, img.get_rect(center = rect.center))

    if on_button:
        if click[0] == 1:
            ra.playAudio(soundFile)


def submitButton(x, y, w, h, img):
    global leaveScreen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, w, h)
    on_button = rect.collidepoint(mouse)

    screen.blit(img, img.get_rect(center = rect.center))

    if on_button:
        if click[0] == 1:
            leaveScreen = True

def choiceButton(x, y, img, num, correct=False):
    global choice
    global selected
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, buttonSizeScale[0], buttonSizeScale[1])
    on_button = rect.collidepoint(mouse)
    
    if selected == num:
        screen.blit(checkmark, checkmark.get_rect(center = rect.center))
    else:
        screen.blit(img, img.get_rect(center = rect.center))

    if on_button:
        screen.blit(checkmark, checkmark.get_rect(center = rect.center))
        if click[0] == 1:
            selected = num
            if correct:
                choice = "correct"
            else:
                choice = "wrong"
    


def talkingHead():
    key = pygame.key.get_pressed()
    if (key[pygame.K_SPACE]):
        screen.blit(speaking, (SCREEN_WIDTH/2.3, SCREEN_HEIGHT/4))
    else:
        screen.blit(notspeaking, (SCREEN_WIDTH/2.3, SCREEN_HEIGHT/4))


title_screen()
recording_screen()
guessing_screen()
end_screen()
pygame.quit()