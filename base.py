import pygame
from random import randint
from pygame.sprite import Group
from settings import Settings
from gamestats import Gamestats
from game_functions import *
from button import Button
from snake import Snake
def run_game():
    pygame.init()
    ssettings=Settings()
    screen=pygame.display.set_mode((ssettings.screen_width,ssettings.screen_height))
    stat=Gamestats(ssettings)
    
    body=[]
    body.append(Snake(screen))
    play_button=Button(screen,ssettings,"Play!")
   
    foods=Group()
    
    pygame.display.set_caption("Snake")
    
    
    
    while True:
        screen.fill(ssettings.bgcolor)
        if not stat.game_active:
            play_button.draw_button()
            reset(body,screen)
        check_events(body,stat,play_button,screen)
        update_screen(body,stat,ssettings,screen,foods)
        

        
run_game()