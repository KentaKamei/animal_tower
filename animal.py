import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# ゲーム画面のサイズと色の設定
screen_width = 800
screen_height = 600
background_color = (255, 255, 255)

# ゲーム画面の作成
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animal Tower Battle")

# 動物の初期位置
animal_x = (screen_width - 50) // 2
animal_y = 10

# 動物の速度
animal_speed = 0.5

#ステージの作成
triangles = []
triangle_quantity = random.randint(5, 12)
origin_x = (screen_width - triangle_quantity * 50) // 2

for i in range(triangle_quantity):
    triangle_vertex_y = random.randint(screen_height * 3 / 4 + 10, screen_height * 3 / 4 + 30)
    triangle_vertex_x =random.randint(origin_x + 10, origin_x + 30)
    triangle_vertices = [(origin_x, screen_height * 3 / 4), (origin_x + 50, screen_height * 3 / 4), (triangle_vertex_x, triangle_vertex_y)]
    triangles.append(triangle_vertices)
    origin_x += 50

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー入力の処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        animal_x -= animal_speed
    if keys[pygame.K_RIGHT]:
        animal_x += animal_speed

    # 背景を描画
    screen.fill(background_color)

    # 動物を描画
    pygame.draw.rect(screen, (255, 0, 0), (animal_x, animal_y, 50, 50))

    # ステージを描画
    for triangle in triangles:
        pygame.draw.polygon(screen, (0, 128, 0), triangle)

    # 画面更新
    pygame.display.update()

# Pygameの終了
pygame.quit()
sys.exit()
