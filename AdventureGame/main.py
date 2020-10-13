import pygame, sys
from sprite import Sprite
import math

def main():
    # Load
    pygame.init()

####
    #crash_sound = pygame.mixer.Sound ("song.mp3")
    pygame.mixer.music.load('song.mp3') 
    pygame.mixer.music.play(- 1)

    #def crash (): ################################# 
    #pygame . mélangeur . Son . jouer ( crash_sound ) 
    #pygame . mélangeur . la musique . stop () ################################## 
    #largeText = pygame . police . SysFont ( "comicsansms" , 115 ) TextSurf , TextRect = text_objects ( "You Crashed" , largeText )
####

    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 24)

    quit = False
    path = 'H:\\Artfx\\Python\\Abygaelle\\AdventureGame\\'

    spr_surface = pygame.image.load('champ.png').convert()
    background = pygame.image.load(path+'fond.png').convert()
    ground = pygame.image.load(path+'sol.png').convert()

    #copain

    copain_x, copain_y = 500,400
    copain_surface = pygame.image.load(path+'ins.png').convert()
    collision_text = font.render("It's treason then!", False, (0,0,0))

    spr_x, spr_y = 100, 435

    cursor = Sprite(0,0,"epee.png")

    spr_is_moving = False

    spr_speed = 0.5
    goal_x = 0

    #hero = Sprite(400, 200, "heroo.png")  
    pygame.mouse.set_visible(False)
    spr_pos = spr_x, spr_y = 100, 400

    while not(quit):
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                goal_x = mouse_click[0]
                #hero.set_position(mouse_click)
                spr_is_moving = True

        # Update
        cursor_pos = pygame.mouse.get_pos()
        cursor.set_position(cursor_pos)
        if(spr_is_moving):
            #spr_pos = mouse_click

            if(spr_x < goal_x): 
                spr_x = spr_x + spr_speed 
            if(spr_x > goal_x): 
                spr_x = spr_x - spr_speed 
            if(math.fabs(goal_x - spr_x) < spr_speed): 
                spr_is_moving = False

        # Draw
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(ground, (0,465))
        #hero.draw(screen)
        screen.blit(copain_surface, (copain_x, copain_y))
        cursor.draw(screen)
        screen.blit(spr_surface, (spr_x,spr_y))
        x1, y1, w1, h1 = spr_x, spr_y, spr_surface.get_width(), spr_surface.get_height()
 
        x2, y2, w2, h2 = copain_x, copain_y, copain_surface.get_width(), copain_surface.get_height()
 
        if(not(x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)):
            screen.blit(collision_text, (spr_x, spr_y - 100))
 
        #screen.blit(cursor, cursor_pos)
        pygame.display.update()

if __name__ =="__main__":
    main()