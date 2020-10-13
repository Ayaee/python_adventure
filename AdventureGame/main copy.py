import pygame, sys, math
from sprite import Sprite

def main():
    # Load
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 24)
    quit = False
    path = 'H:\\Artfx\\Python\\Abygaelle\\AdventureGame\\'
    background = pygame.image.load(path+'background.png').convert()
    hero = Sprite(400, 200, "hero.png")  
    cursor = Sprite(0,0,"cursor.png")
    pygame.mouse.set_visible(False)
    spr_surface = pygame.image.load(path+'hero.png').convert()
    spr_pos = spr_x, spr_y = 100, 400
    ground = pygame.image.load(path+'ground.png').convert()
    spr_x, spr_y = 100, 400
    spr_is_moving = False
    spr_speed = 2
    goal_x = 0
    #get_rect = 100, 0

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
                hero.set_position(mouse_click)
                spr_is_moving = True

        # Update
        cursor_pos = pygame.mouse.get_pos()
        cursor.set_position(cursor_pos)
        if(spr_is_moving):
            spr_x = mouse_click[0]
            mouse_click = pygame.mouse.get_pos()
            goal_x = mouse_click[0]
            spr_is_moving = False
        #position_Sprite = Sprite.get_rect()
        #fenetre.blit(perso, position_perso)

        # Draw
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(ground, (0,500))
        hero.draw(screen)
        cursor.draw(screen)
        pygame.display.update()

if __name__ =="__main__":
    main()