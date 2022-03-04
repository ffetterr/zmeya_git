import pygame
import random
 
# инициализируем pygame
pygame.init()
 
# создаём отображение & запускаем обновление дисплея
width = 640
height = 480
display = pygame.display.set_mode((width, height))
 
pygame.display.update()
pygame.display.set_caption("Игра змейка by Shatunov and Sviridov")
 
# определение цветов
colors = {
    "snake_head": (60, 121, 250),
    "snake_tail": (70, 190, 219),
    "apple": (242, 109, 116)
}
 
# положение змеи стрелочками
snake_pos = {
    "x": width/2-10,
    "y": height/2-10,
    "x_change": 0,
    "y_change": 0
}
 
# размер змеи
snake_size = (10, 10)
 
# текущая скорость движения змеи
snake_speed = 10
 
# Змеиные хвосты
snake_tails = []
 
snake_pos["x_change"] = -snake_speed
for i in range(75):
    snake_tails.append([snake_pos["x"] + 10*i, snake_pos["y"]])
 
# еда
food_pos = {
    "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
}
 
food_size = (10, 10)
food_eaten = 0
 
# начальный цикл
game_end = False
clock = pygame.time.Clock()
 
while not game_end:
    # игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_pos["x_change"] == 0:
                # движение влево
                snake_pos["x_change"] = -snake_speed
                snake_pos["y_change"] = 0
 
            elif event.key == pygame.K_RIGHT and snake_pos["x_change"] == 0:
                # движение вправо
                snake_pos["x_change"] = snake_speed
                snake_pos["y_change"] = 0
 
            elif event.key == pygame.K_UP and snake_pos["y_change"] == 0:
                # движение вверх
                snake_pos["x_change"] = 0
                snake_pos["y_change"] = -snake_speed
 
            elif event.key == pygame.K_DOWN and snake_pos["y_change"] == 0:
                # движение вниз
                snake_pos["x_change"] = 0
                snake_pos["y_change"] = snake_speed
    # очиститка экрана
    display.fill((0,0,0))
