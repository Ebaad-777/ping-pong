import pygame
import random

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('PING PONG')

pygame.font.init()
FONT = pygame.font.Font(None, 36)
back_img = pygame.image.load(r'C:\Users\HP\Downloads\pong.png')
back_img = pygame.transform.scale(back_img, (500, 500))
x = 35
y = 200
w = 30
h = 100
speed = 0.5
x1 = 450
y1 = 200
w1 = 30
h1 = 100
ball_position = [500 // 2, 500 // 2]
bx_speed = 0.2
by_speed = 0.2
opponent_score, player_score = 0, 0

run = True

while run:
    #win.fill((0, 0, 0))
    win.blit(back_img,(0,0))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(win, (255, 255, 255), (x, y, w, h))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if y <= 10:
        y = 10
    elif y >= 390:
        y = 390

    pygame.draw.rect(win, (255, 255, 255), (x1, y1, w1, h1))
    if keys[pygame.K_w]:
        y1 -= speed
    if keys[pygame.K_s]:
        y1 += speed
    if y1 <= 10:
        y1 = 10
    elif y1 >= 390:
        y1 = 390

    # Ball movement
    ball_position[0] += bx_speed 
    ball_position[1] += by_speed 

    # Ball Collision with Top/Bottom Walls
    if ball_position[1] >= 500 or ball_position[1] <= 0:
        by_speed *= -1  # Fix: Reverse direction correctly

    # Ball Collision with Left Paddle
    if (x <= ball_position[0] <= x + w) and (y <= ball_position[1] <= y + h):
        bx_speed *= -1  # Reverse direction

    # Ball Collision with Right Paddle
    if (x1 <= ball_position[0] <= x1 + w1) and (y1 <= ball_position[1] <= y1 + h1):
        bx_speed *= -1  # Reverse direction

    # Ball Out of Bounds (Scoring System)
    if ball_position[0] <= 0:  # Opponent scores
        opponent_score += 1
        ball_position = [250, 250]  # Fix: Reset ball position properly
        bx_speed, by_speed = random.choice([0.2, -0.2]), random.choice([0.2, -0.2])  # Random direction

    if ball_position[0] >= 500:  # Player scores
        player_score += 1
        ball_position = [250, 250]  # Fix: Reset ball position properly
        bx_speed, by_speed = random.choice([0.2, -0.2]), random.choice([0.2, -0.2])  # Random direction
    
    player_score_text=FONT.render(str(player_score),True,'white')
    opponent_score_text=FONT.render(str(opponent_score),True,'white')
    
    win.blit(player_score_text,(500/2+50,50))
    win.blit(opponent_score_text,(500/2-50,50))
    
     

    pygame.draw.circle(win, 'white', ball_position, 10)

    pygame.display.update()

pygame.quit()
