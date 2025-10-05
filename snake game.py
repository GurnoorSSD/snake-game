import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen size
width = 600
height = 400

# Snake settings
snake_block = 10
snake_speed = 8  # Slower snake

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Create screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game 🐍 (No Game Over)")

clock = pygame.time.Clock()

# Score function
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, green)
    screen.blit(value, [0, 0])

# Draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Game loop
def gameLoop():
    game_over = False

    # Starting position
    x1 = width / 2
    y1 = height / 2

    # Movement
    x1_change = snake_block
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Update position
        x1 += x1_change
        y1 += y1_change

        # Reflect on wall collision
        if x1 >= width:
            x1 = width - snake_block
            x1_change = -x1_change
        elif x1 < 0:
            x1 = 0
            x1_change = -x1_change

        if y1 >= height:
            y1 = height - snake_block
            y1_change = -y1_change
        elif y1 < 0:
            y1 = 0
            y1_change = -y1_change

        screen.fill(blue)

        # Draw food
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])

        # Update snake
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        draw_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
gameLoop()
