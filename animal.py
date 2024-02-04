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
animal_x = 375
animal_y = 10

# 動物の速度
animal_speed = 0.5

# ステージの初期設定
stage_width = random.randint(screen_width / 4,screen_width / 4 * 3 )  # ステージの幅をランダムに設定
stage_height = 30  
stage_color = (154, 205, 50)  # ステージの色
stage_x = (screen_width - stage_width) // 2
stage_y = screen_height / 3 * 2

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

    # ステージを描画
    pygame.draw.rect(screen, stage_color, (stage_x, stage_y, stage_width, stage_height))

    # 動物を描画
    pygame.draw.rect(screen, (255, 0, 0), (animal_x, animal_y, 50, 50))

    # 画面更新
    pygame.display.update()

# Pygameの終了
pygame.quit()
sys.exit()
