import pygame
import random

pygame.init()

#game constants
WIDTH = 600
HEIGHT = 500
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)

def getRandomNum():
    return (random.randint(-260, 0))

#game variables 
addedScore = False
score = 0
gravity = 1
active = False
player_x = 50
player_y = 300
y_change = 0
x_change = 0
obstacles = [450, 650, 850]
obstacle_speed = 2
player_running = False
gap = 450
obstacle0_top_start = getRandomNum()
obstacle1_top_start = getRandomNum()
obstacle2_top_start = getRandomNum()


screen = pygame.display.set_mode([WIDTH, HEIGHT])

background = black
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()


#game loop
running = True
while running:
    timer.tick(fps)
    screen.fill(background)
    if not active:
        instruction_text = font.render(f'Space Bar to Start', True, white, black)
        screen.blit(instruction_text, (150, 50))
    

    player = pygame.draw.rect(screen, yellow, [player_x, player_y, 20, 20])
    obstacle0_top = pygame.draw.rect(screen, green, [obstacles[0], obstacle0_top_start, 20, 300])
    obstacle0_bottom = pygame.draw.rect(screen, red, [obstacles[0], obstacle0_top_start + gap, 20, 300])
    obstacle1_top = pygame.draw.rect(screen, green, [obstacles[1], obstacle1_top_start, 20, 300])
    obstacle1_bottom = pygame.draw.rect(screen, red, [obstacles[1], obstacle1_top_start + gap, 20, 300])
    obstacle2_top = pygame.draw.rect(screen, green, [obstacles[2], obstacle2_top_start, 20, 300])
    obstacle2_bottom = pygame.draw.rect(screen, red, [obstacles[2], obstacle2_top_start + gap, 20, 300])

    score_text = font.render(f'Score: {score}', True, white, black)
    screen.blit(score_text, (500, 40))

    if not player_running:
        active = False
        score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        #make reset and start two seperate key pushes

        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles = [450, 650, 850]
                active = True
                player_running = True
                player_x = 50
                player_y = 300
        # if event.type == pygame.KEYDOWN and not player_running:
        #     if event.key == pygame.K_SPACE:
        #         active = True

        #movement player
        if event.type == pygame.KEYDOWN and active and player_running:
            if event.key == pygame.K_SPACE:
                y_change = 12

    #movement obstacles
    for i in range(len(obstacles)):
        if active and player_running:
            obstacles[i] -= obstacle_speed
            if obstacles[i] < -20:
                obstacles[i] = 590
                addedScore = False
                if i == 0:
                    obstacle0_top_start = getRandomNum()
                elif i == 1:
                    obstacle1_top_start = getRandomNum()
                elif i == 2:
                    obstacle2_top_start = getRandomNum()
            if player.colliderect(obstacle0_top) or player.colliderect(obstacle0_bottom) or player.colliderect(obstacle1_top) or player.colliderect(obstacle1_bottom) or player.colliderect(obstacle2_top) or player.colliderect(obstacle2_bottom):
                
                #get HighScore and Print to a file
                file1 = open("highscore.txt", "r+")
                highScore = file1.readline()
                file1.close()
                file1 = open("highScore.txt", "w")
                if int(highScore) < score:
                    file1.write(str(score))
                else:
                    file1.write(str(highScore))
                file1.close()
                player_running = False
                y_change = 0
                x_change = 0

    #jump logic
    if y_change > 0 or player_y < 600:
        player_y -= y_change
        if player_running:
            y_change -= gravity
    #if player_y > 250:
        #player_y = 250
    # if player_y == 500 and y_change < 0:
    #     y_change = 0
    # if player_y < -250:
    #     player_running = False

    if player_y > 500:
        player_running = False
    if player_y < 0:
        player_y = 0

    #track score
    if obstacles[0] < player_x and addedScore == False:
        score+=1
        addedScore = True
    elif obstacles[1] < player_x and addedScore == False:
        score+=1
        addedScore = True
    elif obstacles[2] < player_x and addedScore == False:
        score+=1
        addedScore = True
        
        
    pygame.display.flip()
pygame.quit()