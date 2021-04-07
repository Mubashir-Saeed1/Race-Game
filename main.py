import pygame
import time
from pygame import *
import random

pygame.init()
crash_sound=pygame.mixer.Sound('Crash.wav')
pygame.mixer.music.load('Jazz_In_Paris.wav')
display_width=800
display_height=600
Help=True

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
block_color=(255,128,0)
yellow=(255,255,0)

pause=False
car_width=20
car_height=20

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
Clock=pygame.time.Clock()
carImg=pygame.image.load('car.png')
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

def help_screen():
    gameDisplay.fill(white)
    while Help:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                exit()
                
        text='Instructions:'
        largeText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf,TextRect=text_objects(text,largeText)
        TextRect.center=(155,260)
        gameDisplay.blit(TextSurf,TextRect)
        
        text='Try to Avoid as many boxes as you can.'
        largeText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf,TextRect=text_objects(text,largeText)
        TextRect.center=(280,310)
        gameDisplay.blit(TextSurf,TextRect)

        text='Use Arrow keys to move Your car up,down,right and left.'
        largeText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf,TextRect=text_objects(text,largeText)
        TextRect.center=(365,360)
        gameDisplay.blit(TextSurf,TextRect)
            
        text='Press P to Pause the Game.'
        largeText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf,TextRect=text_objects(text,largeText)
        TextRect.center=(224,414)
        gameDisplay.blit(TextSurf,TextRect)

        gameDisplay.blit(carImg,(380,160))
        pygame.draw.rect(gameDisplay,block_color,(300,40,80,80))
        
        button('Back',300,500,100,50,white,yellow,game_intro)
        pygame.display.update()
        Clock.tick(2)
    
def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text=font.render('Score: '+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def h_score(high):
    font=pygame.font.SysFont(None,25)
    text=font.render('High Score: '+str(high),True,black)
    gameDisplay.blit(text,(670,0))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,block_color,(thingx,thingy,thingw,thingh))

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                exit()

        text='You Crashed'
        largeText=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects(text,largeText)
        TextRect.center=((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf,TextRect)
        
        button('Play Again',150,320,110,50,green,yellow,game_loop)
        button('Exit Game',550,320,110,50,red,yellow,quitgame)
        button('Quit to Main Menu',300,320,200,50,blue,yellow,game_intro)
        
        pygame.display.update()
        Clock.tick(50)
    
    
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText=pygame.font.Font('freesansbold.ttf',20)
    textSurf,textRect=text_objects(msg,smallText)
    textRect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)
    
def quitgame():
    pygame.quit()
    quit()
    exit()

def resume():
    global pause
    pygame.mixer.music.unpause()
    pause=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                paused()
            if event.key==K_p:
                paused()
def paused():
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    resume()
                if event.key==K_p:
                    resume()

        text='Paused'
        largeText=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects(text,largeText)
        TextRect.center=((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf,TextRect)
        
        button('Resume',150,350,100,50,green,yellow,resume)
        button('Quit',550,350,100,50,red,yellow,quitgame)
        
        pygame.display.update()
        Clock.tick(50)
        
def game_intro():
    intro=True
    pause=False
    Help=False
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                exit()

        gameDisplay.fill(white)

        text='A bit Racey'
        largeText=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects(text,largeText)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        
        button('Start',150,450,100,50,green,yellow,game_loop)
        button('Quit',550,450,100,50,red,yellow,quitgame)
        button('Help',350,450,100,50,(255,0,128),yellow,help_screen)

        gameDisplay.blit(carImg,(380,160))
        pygame.draw.rect(gameDisplay,block_color,(300,40,80,80))
        
        pygame.display.update()
        Clock.tick(50)

score=open('high.txt','r')
j=score.read()
k=j
print(k)
if j:
    high_score=int('k')
else:
    high_score=0
    
def game_loop():
    global me
    global score
    global pause
    global high_score
    pygame.mixer.music.play(-1)
    x_change=0
    y_change=0

    x=(display_width * 0.45)
    y=(display_height * 0.8)

    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=5
    thing_width=80
    thing_height=80

    dodged=0
    crashed=False

    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                exit()

            if event.type==KEYDOWN:
                if event.key==K_p:
                    pause=True
                    paused()
                if event.key==K_ESCAPE:
                    paused()

                if event.key==K_LEFT:
                    x_change=-2

                if event.key==K_RIGHT:
                    x_change=2

                if event.key==K_UP:
                    y_change=-2

                if event.key==K_DOWN:
                    y_change=2

            if event.type==KEYUP:
                if event.key==K_LEFT or event.key==K_RIGHT:
                    x_change=0

                if event.key==K_UP or event.key==K_DOWN:
                    y_change=0

        x+=x_change
        y+=y_change

        gameDisplay.fill(white)

        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty+=thing_speed

        car(x,y)
        things_dodged(dodged)

        if x>display_width-car_width or x<0+car_width:
            x_change=0

        if y>display_height-car_height or y<0+car_height:
            y_change=0

        if thing_starty==display_height:
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            dodged+=1
        if dodged>high_score:
            high_score=dodged
            highs=open('high.txt','w')
            highs.write(f'{high_score}')
            highs.close()
            
        highs=open('high.txt','r')
        no=highs.read()
        h_score(no)

        if y<thing_starty+thing_height and y>thing_starty:
            if x>thing_startx-(2*car_width) and x<thing_startx+thing_width:
                crash()

        pygame.display.update()
        Clock.tick(1000)

game_intro()
game_loop()
pygame.quit()
quit()
exit()
