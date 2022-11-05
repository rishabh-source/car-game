import pygame
import random
import time
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("buggy.mp3")
pygame.mixer.music.play(-1)

display_width = 500
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)
i=0

clock = pygame.time.Clock()
crashed = False
road = pygame.image.load('road.png')
road=pygame.transform.scale(road,(750,1550))
road1= pygame.image.load('road.png')
road1=pygame.transform.scale(road,(750,1550))

carImg = pygame.image.load('racecar.png')
carImg=pygame.transform.scale(carImg,(80,80))
d=0
def car(x,y):
    global d,s
    d=(display_width * 0.5)+x
    s=(display_height * 0.8)+y
    gameDisplay.blit(carImg, (d,s))
def roadrun(x,y):
	global i
	if y>1500:
		i=0
		gameDisplay.blit(road,(0,y))
	else:
		gameDisplay.blit(road,(0,y))
		
def roadrun1(x,y):
	global i
	if y>1500:
		i=0
		gameDisplay.blit(road,(0,y))
	else:
		gameDisplay.blit(road,(0,y))
a=0
k=0
j=0		
prob=random.random()
cars=random.choice(('yellowcar.png','bluecar.png','greencar.png'))
while not crashed:
    i=i+a
    a=a+0.01
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.MOUSEBUTTONUP:
        	pos= pygame.mouse.get_pos()
        	if pos[0]<500 and d>100:
        		k=k-100
        	elif pos[0]>500 and d<500:
        		k=k+100
    gameDisplay.fill(black)
    roadrun(0,i)
    roadrun1(0,i-1500)
    car(k,300)    
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render('Score:'+str(int(a)), True, white,black)
    textRect = text.get_rect()
    textRect.center = (100,50)
    if prob<1:
    	j=j+a
    	enemy= pygame.image.load(cars)
    	enemy=pygame.transform.scale(enemy,(80,80))
    	gameDisplay.blit(enemy,(prob*500,j))
    	if j>1500:
    		j=0
    		prob=random.random()
    		cars=random.choice(('yellowcar.png','bluecar.png','greencar.png'))
    		gameDisplay.blit(enemy,(prob*500,j))
    	if abs(prob*500-d)<80 and abs(s-j)<80:
    		crashed=True
    gameDisplay.blit(text,textRect)
    pygame.mixer.music.set_volume(0.1+a/50)
    pygame.display.update()
    
while crashed:
	font = pygame.font.SysFont('georgia', 60)
	text = font.render('CØNGRATULATIONS', True, white,black)
	text1= font.render('YØUR SCØRE IS '+str(int(a)), True, white,black)
	textRect = text.get_rect()
	textRect1=text1.get_rect()
	textRect.center = (350,300)
	textRect1.center=(350,400)
	gameDisplay.blit(text,textRect)
	gameDisplay.blit(text1,textRect1)
	pygame.mixer.music.play()
	pygame.display.update()
	
	