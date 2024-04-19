import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000 )- start_time
    
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(bottomleft=(100,100))
    screen.blit(score_surf,score_rect)


pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Kitty')

gameIcon =  pygame.image.load('Icon/cat_icon.jpg')
pygame.display.set_icon(gameIcon)

#display gibt es nur 1x  und darauf sind alle anderen sachen plaziert , wie eine pinwand

clock = pygame.time.Clock()

test_font = pygame.font.Font('Font/Pixeltype.ttf',50)
test_font2 = pygame.font.Font('Font/Pixeltype.ttf',50)


sky_surface = pygame.image.load('Background/background.webp').convert()

ground_surface = pygame.image.load('Ground/ground.jpg').convert()

#score_surface = test_font.render('Points ',False,(64,64,64))
#score_surf_rect = score_surface.get_rect(bottomleft=(100,100))


slime_surface_right = pygame.image.load('Enemy/slime_red.png').convert_alpha()
slime_surf_rect = slime_surface_right.get_rect(bottomleft = (1000,400))
slime_surf_left = pygame.transform.flip(slime_surface_right,True,False)
slime_surf_left_rect =slime_surf_left.get_rect(bottomleft = (1000,400))
#slime_surf_left_rect = pygame.transform.flip(slime_surf_right_rect,True,False)  
#slime von rechts auf links drehen (surface, xBool, yBool)
 
player_surface = pygame.image.load('Cat/player.png').convert_alpha()
player_rectangle = player_surface.get_rect(bottomleft = (10,400))

player_gravity = 0

game_active = True
start_time = 0

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >=400:
                    player_gravity = -25


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >=400:
                    player_gravity = -25

        else:
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                game_active = True
                slime_surf_left_rect.left = 1000
                start_time = int(pygame.time.get_ticks() / 1000 )- start_time


    if game_active:
        screen.blit(sky_surface,(0,-80))  
        screen.blit(ground_surface,(0,400))
        screen.blit(ground_surface,(512,400))

        #pygame.draw.rect(screen,'#c0e8ec',score_surf_rect,)
        #pygame.draw.rect(screen,'#c0e8ec',score_surf_rect,10)
        #screen.blit(score_surface,score_surf_rect)

        display_score()

        screen.blit(slime_surf_left,slime_surf_left_rect)
        slime_surf_left_rect.x -=4
        if slime_surf_left_rect.x < -50:
            slime_surf_left_rect.x = 1000


        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 400:
            player_rectangle.bottom = 400
       

        screen.blit(player_surface,(player_rectangle))

        if slime_surf_left_rect.colliderect(player_rectangle):
            screen.fill('Red')

            gameOver_surface = test_font.render('Press Space to Restart ',False,(64,64,64))
            gameName_surface= test_font.render('Pixel Runner',False,(64,64,64))

            screen.blit (player_surface,(500,200))

            gameOver_surf_rect = gameOver_surface.get_rect(bottomleft=(300,200))

            screen.blit(gameOver_surface,gameOver_surf_rect)
            screen.blit(gameName_surface,(350,400))


            game_active = False
           

    pygame.display.update()
    clock.tick(60)  # while loop will not run faster then 60 fps
    