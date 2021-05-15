# Simple Snake Game
# By Beau J Calrk
# Python 3.8.9
# Pygame 2.0.1

# The object of the game is to eat ass much fruit as you can with out 
# touching the screen edges or colliding with yourself.

import pygame
import sys
import time
import random
import keyboard
from pygame.locals import *

# Set up colors to be used
BLACK = pygame.Color(0,0,0)
GREEN = pygame.Color(0,255,0)
RED = pygame.Color(255,0,0)

# initial starting point for the dot the snake eats
dot_x_cord = 100
dot_y_cord = 100

# Initial starting point, sarting length and snake_speed for snake. 
snake_pos = [random.randrange(50, 500), random.randrange(50, 600)]
snake_body_list = [[200, 70], [170, 70],[140, 70]]
snake_speed = 10

# Initial starting snake_direction for snake
snake_direction = "right"

pygame.init()

# Set up fame limits for game
FPS = 30
clock = pygame.time.Clock()

window_size = width, height = 600, 700
main_window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snake")

score = 0
score_font = pygame.font.Font('freesansbold.ttf', 15)
score_rect = pygame.Rect(10, 10, 10, 10)

def start():
    ready_message = ('Ready')
    ready_message_font = pygame.font.Font('freesansbold.ttf', 30)
    ready_text = ready_message_font.render(ready_message, True, RED)
    ready_message_rect = pygame.Rect(250, 300, 50, 50)
    main_window.blit(ready_text, ready_message_rect)
    pygame.display.update()
    time.sleep(2)

def game_over():
    game_over_message = ('Game Over')
    game_over_message_font = pygame.font.Font('freesansbold.ttf', 30)
    game_over_message_text =  game_over_message_font.render(game_over_message, True, RED)
    game_over_message_rect = pygame.Rect(210, 300, 50, 50)
    main_window.blit(game_over_message_text, game_over_message_rect)
    pygame.display.update()
    time.sleep(2)

start()
while True:
    
    main_window.fill(BLACK)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit(), sys.exit()

        # change the snake_direction of the snake. 
        if keyboard.is_pressed('right') and snake_direction != "left":
            snake_direction = 'right'

        elif keyboard.is_pressed('left')and snake_direction != "right":
            snake_direction = 'left'

        elif keyboard.is_pressed('up')and snake_direction != "down":
            snake_direction = 'up'

        elif keyboard.is_pressed('down')and snake_direction != "up": 
            snake_direction = 'down'

    # Make the snake costantly move in a direction and keep it inside the window. 
    if snake_direction == "right" and snake_pos[0] <= 570:
        snake_pos[0] += snake_speed

    elif snake_direction == 'left' and snake_pos[0] >= 5:
        snake_pos[0] -= snake_speed

    elif snake_direction == 'up' and snake_pos[1] >= 20:
        snake_pos[1] -= snake_speed

    elif snake_direction == 'down' and snake_pos[1] <= 670:
        snake_pos[1] += snake_speed

    # Draw the body of the snake
    for snake_piece in snake_body_list:
        snake_body_rect = pygame.draw.rect(main_window, GREEN, pygame.Rect(snake_piece[0], snake_piece[1], 20, 20))

    # update the snake body list with its position
    snake_body_list.append(list(snake_pos))# add the new position to the snake body list. This will allow the snake to move.

    # Check to see if snake collides with its self. If it does end the game. Game will also end if snake touches the edge of
    # the screen due to the snake collapsing in on it self and then colliding with its self. 
    for part in snake_body_list[:-3]:#If the last 3 indexes are not ommited the snake will costantly collide with its self. 
        if pygame.Rect.colliderect(pygame.Rect(part[0], part[1], 20, 20), pygame.Rect(snake_pos[0], snake_pos[1], 20, 20)):
            game_over()
            pygame.quit(), sys.exit()

    #Check to see if snake collides with dot and add one to score if it does
    if pygame.Rect.colliderect(snake_body_rect, pygame.Rect(dot_x_cord, dot_y_cord, 20, 20)):
        dot_x_cord = random.randrange(5, 570)
        dot_y_cord = random.randrange(5, 670)
        score += 1
    else:
        snake_body_list.pop(0)# Delete the last position so to not draw a constant line
    
    pygame.draw.rect(main_window, RED, pygame.Rect(dot_x_cord, dot_y_cord, 20, 20))

    # update the score to the screen 
    score_text = score_font.render(str(score), True, RED)
    main_window.blit(score_text, score_rect)
    
    pygame.display.flip()
    clock.tick(FPS)