import pygame
import random
pygame.init()

''' 
A source used
https://pygame.readthedocs.io/en/latest/1_intro/intro.html

add youtube vid source link
'''
black = (0, 0, 0)
green = (112, 175, 46)
red = (235, 26, 26)
white = (255, 255, 255)

display_width, display_height = 800, 600 # or 1200, 900 for block size 50
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
fps, block = pygame.time.Clock(), 25
font_style, score_font = pygame.font.SysFont("arial", 35), pygame.font.SysFont("arial", 40)

def snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], block, block])

def message(msg, color):
    messg = font_style.render(msg, True, color)
    display.blit(messg, [display_width / 10, display_height / 3]) # centers text for display of 800, 600
def player_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    display.blit(value, [0, 0]) 
def get_high_score():
    try:
        with open("highscore.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
    return high_score

def update_high_score(score):
    high_score = get_high_score()
    if score > high_score:
        with open("highscore.txt", "w") as file:
            file.write(str(score))
def player_high_score():
    high_score = get_high_score()
    value = score_font.render("High Score: " + str(high_score), True, white)
    display.blit(value, [0, 40])

def game():
    game_over = False
    game_close = False
    x1 = display_width / 2
    y1 = display_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    snake_length = 1
    food_x = round(random.randrange(0, display_width - block,) / block) * block
    food_y = round(random.randrange(0, display_height - block) / block) * block

    while not game_over:
        fps.tick(12)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != block:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -block:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != block:
                    y1_change = -block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -block:
                    y1_change = block
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(green)
        pygame.draw.rect(display, red, [food_x, food_y, block, block])

        if len(snake_List) > snake_length:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(block, snake_List)
        player_score(snake_length - 1)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, display_width - block,)/ block) * block
            food_y = round(random.randrange(0, display_height - block)/ block) * block
            snake_length += 1

        if game_close:
            display.fill(green)
            message("You Lost! Press P-Play Again or Q-Quit", white)
            player_score(snake_length - 1)
            player_high_score()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            return False
                        if event.key == pygame.K_p:
                            return True
    pygame.quit()
    return False
while game():
    pass