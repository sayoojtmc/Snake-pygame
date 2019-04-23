import pygame
from random import randint
import os
cwd =os.getcwd()
from pygame.sprite import Sprite
class Snake(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load(os.path.join(cwd,"images/piece.png"))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.centerx=randint(0,1000)
        self.rect.centery=randint(0,800)

        self.direction=0
        self.length=0

        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.updatecount=0
    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def update(self,ssettings):



        self.rect.x=self.x
        self.rect.y=self.y
