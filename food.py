import pygame
from random import randint
from pygame.sprite import Sprite
import os
cwd =os.getcwd()
class Food(Sprite):
    def __init__(self,ssettings):
        super().__init__()
        self.image=pygame.image.load(os.path.join(cwd,"images/food.png"))
        self.rect=self.image.get_rect()
        self.rect.centerx=randint(50,ssettings.screen_width-50)
        self.rect.centery=randint(50,ssettings.screen_height-50)
