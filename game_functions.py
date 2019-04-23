import sys
import pygame
from food import Food
from snake import Snake
from random import randint
import os
cwd =os.getcwd()
def check_events(body,stats,play_button,screen):
     for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        stats.game_active=True
                        reset(body,screen)
                    if event.key==pygame.K_q:
                        sys.exit()
                    if event.key==pygame.K_d:

                        if body[0].direction==1:

                            continue
                        else:
                            body[0].direction=0
                    elif event.key==pygame.K_a:
                        if body[0].direction==0:
                            continue
                        else:
                            body[0].direction=1
                    elif event.key==pygame.K_w:
                        if body[0].direction==3:
                            continue
                        else:
                            body[0].direction=2
                    elif event.key==pygame.K_s:
                        if body[0].direction==2:
                            continue
                        else:
                            body[0].direction=3
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                check_play(stats,play_button,mouse_x,mouse_y,screen,body)

def check_play(stats,play_button,mouse_x,mouse_y,screen,body):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
        reset(body,screen)
def grow(body,screen):
        block=Snake(screen)
        block.rect.x,block.rect.y=-10,-10
        body.append(block)
def check_fail(stats,body,ssettings,screen,foods):
    for i in range(5,len(body)):
        if body[0].rect.collidepoint(body[i].rect.center):
            stats.game_active=False


def reset(body,screen):
    del body[1:]
    body=[]

    body.append(Snake(screen))
    body[0]=Snake(screen)
    body[0].x=randint(0,1000)
    body[0].x=randint(0,800)




def update_screen(body,stats,ssettings,screen,foods):

    body[0].update(ssettings)


    if len(foods)<1:
        create_food(foods,ssettings)
    foods.draw(screen)
    check_fail(stats,body,ssettings,screen,foods)
    if stats.game_active==True:
        change_direction(body,stats,ssettings)
    else:
        reset(body,screen)
    if pygame.sprite.pygame.sprite.pygame.sprite.spritecollideany(body[0], foods):
        eat_food(foods)
        grow(body,screen)
        grow(body,screen)


    body[0].blitme()
    for i in range(0,len(body)-1):
        body[i].blitme()
    pygame.display.flip()

def create_food(foods,ssettings):
    food=Food(ssettings)
    foods.add(food)
def eat_food(foods):
    foods.empty()

def make_border(screen):
    image=pygame.image.load(os.path.join(cwd,"images/border.png"))
    rect=image.get_rect()
    rect.center=screen.get_rect().center
    screen.blit(image,rect)
def change_direction(body,stats,ssettings):
    body[0].updatecount+=1
    if(body[0].updatecount>20):
        for i in range(len(body)-1,0,-1):



            body[i].rect.x=body[i-1].rect.x
            body[i].rect.y=body[i-1].rect.y
        body[0].updatecount=0


    if(body[0].direction==0):
        if(body[0].rect.right<ssettings.screen_width):
            body[0].x+=ssettings.snake_speed
        else:
            stats.game_active=False
    if(body[0].direction==1):
        if(body[0].rect.x>0):
            body[0].x-=ssettings.snake_speed
        else:
            stats.game_active=False
    if(body[0].direction==2):
        if(body[0].rect.y>0):
            body[0].y-=ssettings.snake_speed
        else:
            stats.game_active=False
    if(body[0].direction==3):
        if(body[0].rect.bottom<ssettings.screen_height):
            body[0].y+=ssettings.snake_speed
        else:
            stats.game_active=False
