import pygame

#initialising pygame engine
pygame.init()

#import os
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

# constants
WIDTH, HEIGHT = 800, 400
GROUND_HEIGHT = 100
FPS = 60

# colours
WHITE = (255, 255, 255)

# create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("subway surfers")

# load game assessts (character and obsticles)
player_img = pygame.image.load("player.png")
obsticle_img = pygame.image.load("train_drawing_2d_view_of_transportation_units_dwg_file_26022019045218.webp")

# player variables
player_x = WIDTH // 2
player_y = HEIGHT - GROUND_HEIGHT - player_img.get_height()
player_speed = 5
player_jump = False
jump_height = 20

# obsticle variables
obsticle_x = WIDTH
obsticle_y = HEIGHT - GROUND_HEIGHT - obsticle_img.get_height()
obsticle_speed = 3

# score
score = 0

# game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # handeling player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_RIGHT] and not player_jump:
            player_jump = True

        # player jump and fall
        if player_jump:
            player_y -= jump_height
            jump_height -= 1
            if jump_height < -15:
                player_jump = False
                jump_height = 15
        else:
            if player_y < HEIGHT - GROUND_HEIGHT - player_img.get_height():
                player_y += jump_height
                jump_height += 1
            else:
                player_y = HEIGHT - GROUND_HEIGHT - player_img.get_height()
                jump_height = 15

# move obs
obsticle_x -= obsticle_speed

# check for collisions
player_react = pygame.Rect(player_x, player_y, player_img.get_width(), player_img.get_height())
obstacle_react = pygame.Rect(obsticle_x, obsticle_y, obsticle_img.get_width(), obsticle_img.get_height())

if player_react.colliderect(obstacle_react):
    running = False

# update
score += 1

# draw everything
screen.fill(WHITE)
screen.blit(player_img, (player_x, player_y))
screen.blit(obsticle_img, (obsticle_x, obsticle_y))

# display score
font = pygame.font.Font(None, 36)
score_text = font.render(f"Score: {score}", True, (0,0,0))
screen.blit(score_text, (10,10))
pygame.display.flip()

# check if obs is off screen
if obsticle_x < -obsticle_img.get_width():
    obsticle_x = WIDTH 
    obsticle_y = HEIGHT - GROUND_HEIGHT - obsticle_img.get_height()

clock.tick(FPS)

# game over screen
font = pygame.font.Font(None, 72)
game_over_text = font.render("Game, over", True, (255,0,0))
screen.blit(game_over_text, (WIDTH //2 - 150, HEIGHT //2 - 50))
pygame.display.flip()

pygame.time.delay(2000)
pygame.quit()