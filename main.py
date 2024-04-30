import pygame
import time
import random

# Setup
pygame.init()
win_width = 1200
win_height = 800

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

snake_block = 20
snake_list = []

# Load images
food_image = pygame.image.load('apple.jpg')
food_image = pygame.transform.scale(food_image, (snake_block, snake_block))

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def score(score):
    value = score_font.render("Your Score: " + str(score), True, (255, 255, 255))  # Change text color to white
    win.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, (0, 255, 0), [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [win_width / 3, win_height / 3])

def gameLoop():  
    game_over = False
    game_close = False

    # starting coordinates for the snake
    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    # snake body
    snake_List = []
    Length_of_snake = 1

    # positions of food
    foodx = round(random.randrange(0, win_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, win_height - snake_block) / snake_block) * snake_block

    clock = pygame.time.Clock()
    snake_speed = 5  # Start with a slower speed

    while not game_over:
        while game_close == True:
            win.fill((100,100,100))
            message("You Lost! Press Esc-Quit or Enter-Play Again", (255, 0, 0))  
            score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_RETURN:  
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    if y1_change == 0:  # Check if the snake is not already moving down
                        y1_change = -snake_block
                        x1_change = 0
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    if y1_change == 0:  # Check if the snake is not already moving up
                        y1_change = snake_block
                        x1_change = 0
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    if x1_change == 0:  # Check if the snake is not already moving right
                        x1_change = -snake_block
                        y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    if x1_change == 0:  # Check if the snake is not already moving left
                        x1_change = snake_block
                        y1_change = 0

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        win.fill((0,0,0))  
        win.blit(food_image, (foodx, foody))  # Draw food image
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, win_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
            snake_speed +=.7  # Increase the speed every time the snake eats food

        clock.tick(snake_speed)  # Modify the game speed based on the variable snake_speed

    pygame.quit()
    quit()

gameLoop()