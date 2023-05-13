from pygame import *
from random import randint

mixer.init()
font.init()
win = display.set_mode((1000,700))
display.set_caption('PingPong')
bg = transform.scale(image.load('fon.Pong.jpg'), (1000, 700))
clock = time.Clock()



run = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, pic, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(pic), (w,h))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Hero(GameSprite): 
    def update1(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < 650:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < 650:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.x <= 0:
            self.kill()
        if self.rect.x >= 1000:
            self.kill()
        

hero1 = Hero(900,350,100,200,'rocketka1.png',10)
hero2 = Hero(0,350,100,200,'rocketka1.png',10)
ball =  Ball(500,350,70,70, 'Ball.png', 1)


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
            
    if not finish:
           
        win.blit(bg, (0, 0))
        hero1.reset()
        hero1.update1()
        hero2.reset()
        hero2.update2()
        ball.update()
        ball.reset()  
        if sprite.groupcollide(ball, hero1, True, True):
        
        if sprite.groupcollide(ball, hero2, True, True):
    
    display.update()
    clock.tick(60)
'''
    for e in event.get():
            if e.type == K_r:
                run = True
                finish = False
            '''