import pygame
import sys
import random
import pymunk

# Pygameの初期化
pygame.init()

# ゲーム画面のサイズと色の設定
screen_width = 800
screen_height = 600
background_color = (255, 255, 255)

# ゲーム画面の作成
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animal Tower Battle")

# 動物の速度
animal_speed = 0.05

# 物理エンジンの初期化
space = pymunk.Space()
space.gravity = (0, -0.5)  # 重力の設定

# 物理ボディの作成
def create_animal(space, x, y):
    body = pymunk.Body(1, 100)  # 質量1, 慣性モーメント100
    body.position = (screen_width - 50) // 2, screen_height - 50  # 初期位置
    shape = pymunk.Poly.create_box(body, (50, 50))  # 矩形の形状
    shape.friction = 0.7 
    shape.elasticity = 0.3
    space.add(body, shape)  # 物理エンジンに追加
    return body, shape

def reset_animal(space, body):
    space.remove(body, body.shapes[0])  # 現在の動物を削除
    return create_animal(space, (screen_width - 50) // 2, screen_height - 50)  # 新しい動物を生成

#初期動物を生成
body, shape = create_animal(space, (screen_width - 50) // 2, screen_height - 50)

#ステージの作成
triangles = []
triangle_quantity = random.randint(5, 12)
origin_x = (screen_width - triangle_quantity * 50) // 2


for i in range(triangle_quantity):
    triangle_vertex_y = random.randint(screen_height * 3 / 4 + 15, screen_height * 3 / 4 + 30)
    triangle_vertex_x =random.randint(origin_x + 10, origin_x + 30)
    triangle_vertices = [(origin_x, screen_height * 3 / 4), (origin_x + 50, screen_height * 3 / 4), (triangle_vertex_x, triangle_vertex_y)]
    triangles.append(triangle_vertices)
    origin_x += 50

# ステージの物理ボディを作成
for triangle in triangles:
    stage_body = pymunk.Body(body_type=pymunk.Body.STATIC)  # 静的ボディ
    converted_triangle = [(vertex[0], screen_height - vertex[1]) for vertex in triangle]
    stage_shape = pymunk.Poly(stage_body, converted_triangle)
    stage_shape.elasticity = 0.7  # 弾性
    stage_shape.friction = 0.7
    space.add(stage_body, stage_shape)


clicked = False

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = True  # クリックされたらフラグをTrueにする


    # キー入力の処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        body.position -= (animal_speed, 0)
    if keys[pygame.K_RIGHT]:
        body.position += (animal_speed, 0)

    # クリックされるまで物理エンジンのステップを実行しない
    if clicked:
        # 物理エンジンのステップを実行
        dt = 1 / 120  # 60 FPSで更新
        space.step(dt)

    # 物体が画面下に落下したかチェック
    if body.position.y < 0:
        running = False

    # 背景を描画
    screen.fill(background_color)

    # 動物を描画
    pos_x, pos_y = body.position
    angle = body.angle
    pygame.draw.rect(screen, (255, 0, 0), (pos_x - 25, screen_height - pos_y - 25, 50, 50))  # ボディを描画

    # ステージを描画
    for triangle in triangles:
        pygame.draw.polygon(screen, (0, 128, 0), triangle)

    # 画面更新
    pygame.display.update()

# Pygameの終了
pygame.quit()
sys.exit()
