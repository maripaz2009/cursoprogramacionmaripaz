








import math 
import random
import pygame

from pygame import mixer 

# inicio del juego 
pygame.int()

# se crea el fondo de pantalla 
screen = pygame.display.set_mode((1000,800))

#fondo de pantalla 
background = pygame.image.load("/home/pc16/Descargas/juego/Fondo.png")

# sonido de fondo 
mixer.music.load("/home/pc16/Descargas/juego/sonido fondo.mp4")
mixer.music.play(-1)

# titulo y icono 
pygame. display.set_caption ("Perdidos en sigma land") 
icon = pygame.mage.load("/home/pc16/Descargas/juego/Enemigo 2.png")
pygame.display.set_icon(icon)

#jugador
PlayerImg=pygame.image.load("/home/pc16/Descargas/juego/nave .png")
playerX= 370
playery =480
playerX_change=0

#enemigos
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies= 30

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("/home/pc16/Descargas/juego/enemigo 1.png"))
    enemyX.append(random.randint(0.736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#disparo, proyectil, bala 

armaImg= pygame.image.load("/home/pc16/Descargas/juego/Bala. png")
armaX=0
armaY=480
armaX_change=0
armaY_change=10
arma_estado="ready"

#puntaje
 
score_value=0
font =pygame.font.Font('freesansbold.ttf,32')


textX=10
textX=10

#juego teminado
over_font =pygame.font.Font('freesansbold.ttf, 64')

def show_puntaje(x,y):
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score(x,y))
def gameover_text():
    over_text= over_font.render("GameOver", True,255,255,255)
    screen.blit(over_text,(200,250))
def player (x,y):
    screen.blit(PlayerImg,x,y)
def enemy (x,y,i):
    screen.blit(enemyImg(i),(x,y))
def Iniciar_disparo(x,y):
        global arma_estado
        arma_estado ="Fire"
        screen.blit(armaImg,(x+16,+10))
def iscollision(enemyX,enemyY,armaX,armaY): 
        distance= math.sqrt(math.pow(enemyX-armaX)+(math.pow(enemyY-armaY,2))) 
        if distance<27:
             return True
        else: return False

# game loop
running = True
while running:
     screen.fill((0,0,0))
     #imagen de fondo
     screen.blit(background,(0,0))
     for event in pygame.event.get():
          if event.type == pygame.quit:
               running =False


               # si presiona derecha o izquierda
               if event.type==pygame.KEYDOWN:
                    if  event.key==pygame.K_LEFT:
                         playerX_change=-5
                         if event.key==pygame.K_RIGHT:
                              player_change= 5
                             if event.key == pygame.
                              
