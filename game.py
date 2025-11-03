import pygame
import random

pygame.display.set_caption('Snake Game')
pygame.init()

font = pygame.font.Font(None, 72)

orange = (255, 69, 0)
white = (255, 255, 255)
purple = (48, 25, 52)

clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 800))

pix_size = 40

snake_x = 400
snake_y = 400
fruit_x = random.randint(1, 18) * pix_size
fruit_y = random.randint(1, 18) * pix_size


dx = 0
dy = 0

snakeBody = []
snakeLength = 1

running = True

while running:        
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    
    window.fill(purple)
    
    pygame.draw.rect(window, white, [snake_x, snake_y, pix_size, pix_size])
    pygame.draw.rect(window, orange, [fruit_x, fruit_y, pix_size, pix_size])
    
    # snake sides
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            dx = -pix_size
            dy = 0
        
        elif event.key == pygame.K_RIGHT:
            dx = pix_size
            dy = 0
        
        elif event.key == pygame.K_UP:
            dy = -pix_size
            dx = 0
            
        elif event.key == pygame.K_DOWN:
            dy = pix_size
            dx = 0
                
        
    snake_x += dx
    snake_y += dy
        
    # map limits
    if snake_x > 800 - pix_size:
        snake_x = 0
        
    elif snake_x < 0:
        snake_x = 800 - pix_size
        
    elif snake_y > 800 - pix_size:
        snake_y = 0

    elif snake_y < 0:
        snake_y = 800 - pix_size
    
    snakeHead = []

    snakeHead.append(snake_x)
    snakeHead.append(snake_y)
    snakeBody.append(snakeHead)

    if len(snakeBody) > snakeLength:
        del snakeBody[0]
            
    if fruit_x == snake_x and fruit_y == snake_y:
        fruit_x = random.randint(1, 18) * pix_size
        fruit_y = random.randint(1, 18) * pix_size

        snakeLength += 1

    if [snake_x, snake_y] in snakeBody[:-1]:
        break
        
        
    for pixel in snakeBody:
        pygame.draw.rect(window, white, [pixel[0], pixel[1], pix_size, pix_size])

    pygame.draw.rect(window, orange, [fruit_x, fruit_y, pix_size, pix_size])
    pygame.display.update()

    clock.tick(10)
pygame.quit()
