import pygame
from random import randint
from pygame.sprite import Sprite
class Food(Sprite):
    def __init__(self,ssettings):
        super().__init__()
        self.image=pygame.image.load("/home/sayooj/Documents/Snake/images/food.png")
        self.rect=self.image.get_rect()
        self.rect.centerx=randint(50,ssettings.screen_width-50)
        self.rect.centery=randint(50,ssettings.screen_height-50)

