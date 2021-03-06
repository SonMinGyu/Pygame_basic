import pygame
import random

pygame.init()  # 초기화(반드시 해야함)

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("make_my_game")  # 게임이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)  # 현재 파일 위치 반환
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "background1.png"))

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    os.path.join(image_path, "dog2.png"))
character_size = character.get_rect().size  # 캐릭터 사이즈 가져오기
character_width = character_size[0]  # 캐릭터 가로크기
character_height = character_size[1]  # 캐릭터 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 가운데
character_y_pos = screen_height - character_height  # 화면 세로의 바닥

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 1

# 적 enemy 캐릭터
enemy = pygame.image.load(
    os.path.join(image_path, "bone.png"))
enemy_size = enemy.get_rect().size  # 캐릭터 사이즈 가져오기
enemy_width = enemy_size[0]  # 캐릭터 가로크기
enemy_height = enemy_size[1]  # 캐릭터 세로크기
enemy_x_pos = 0 + random.randrange((screen_width - enemy_height))
enemy_y_pos = 0 - enemy_height
enemy_speed = 1

# 적 enemy2 캐릭터
enemy2 = pygame.image.load(
    os.path.join(image_path, "bone.png"))
enemy2_size = enemy2.get_rect().size  # 캐릭터 사이즈 가져오기
enemy2_width = enemy2_size[0]  # 캐릭터 가로크기
enemy2_height = enemy2_size[1]  # 캐릭터 세로크기
enemy2_x_pos = 0 + random.randint(0, (screen_width - enemy_height))
enemy2_y_pos = 0 - enemy_height - random.randrange(100)
enemy2_speed = 1

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성

# 받은 수
receive_number = 0

# # 총 시간
# total_time = 10

# # 시작 시간
# start_ticks = pygame.time.get_ticks()  # 시작 ticks를 받아옴

# 이벤트 루프
running = True  # 게임이 진행중인가
while running:
    dt = clock.tick(120)  # 게임화면의 초당 프레임 수 설정

    for event in pygame.event.get():  # 어떤 이벤트 발생?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 실행시
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        to_x -= character_speed
        character_x_pos += to_x * dt
        if character_x_pos < 0:
            character_x_pos = 0
        to_x = 0
    if keys[pygame.K_RIGHT]:
        to_x += character_speed
        character_x_pos += to_x * dt
        if character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
        to_x = 0
    if keys[pygame.K_UP]:
        to_y -= character_speed
        character_y_pos += to_y * dt
        if character_y_pos < 0:
            character_y_pos = 0
        to_y = 0
    if keys[pygame.K_DOWN]:
        to_y += character_speed
        character_y_pos += to_y * dt
        if character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height
        to_y = 0

    if enemy_y_pos > screen_height:
        enemy_x_pos = 0 + random.randint(0, (screen_width - enemy_height))
        enemy_y_pos = 0 - enemy_height

    if enemy2_y_pos > screen_height:
        enemy2_x_pos = 0 + random.randint(0, (screen_width - enemy_height))
        enemy2_y_pos = 0 - enemy_height

    enemy_y_pos += enemy_speed * dt
    enemy2_y_pos += enemy_speed * dt

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        enemy_x_pos = 0 + random.randint(0, (screen_width - enemy_height))
        enemy_y_pos = 0 - enemy_height
        receive_number += 1
        if receive_number == 20:
            print("성공!")
            running = False

    if character_rect.colliderect(enemy2_rect):
        enemy2_x_pos = 0 + random.randint(0, (screen_width - enemy_height))
        enemy2_y_pos = 0 - enemy_height
        receive_number += 1
        if receive_number == 20:
            print("성공!")
            running = False

    # screen.fill((0,0,255)) #배경화면 색으로 채우기 (R,G,B)값
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))

    score = game_font.render(str(receive_number), True, (0, 0, 0))
    screen.blit(score, (10, 10))
########################################################################################################
    # # 타이머 집어넣기
    # # 경과 시간 계산
    # elapsed_time = (pygame.time.get_ticks() - start_ticks) / \
    #     1000  # 경과시간을 1000으로 나누어 초 단위로 표시

    # timer = game_font.render(
    #     str(int(total_time - elapsed_time)), True, (255, 255, 255))  # 출력할 글자, True, 글자 색상

    # screen.blit(timer, (10, 10))

    # 시간이 0 이하이면 게임 종료
    # if total_time - elapsed_time <= 0:
    #     print("타임아웃")
    #     running = False
########################################################################################################

    pygame.display.update()  # 게임화면 다시 그리기

# 종료 전 잠시 대기
pygame.time.delay(2000)  # 2초 대기

# pygame 종료
pygame.quit()
