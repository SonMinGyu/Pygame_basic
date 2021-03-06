import pygame

pygame.init()  # 초기화(반드시 해야함)

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("make_my_game")  # 게임이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load(
    "C:\\Users\\littl\\OneDrive\\바탕 화면\\python\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    "C:\\Users\\littl\\OneDrive\\바탕 화면\\python\\pygame_basic\\character.png")
character_size = character.get_rect().size  # 캐릭터 사이즈 가져오기
character_width = character_size[0]  # 캐릭터 가로크기
character_height = character_size[1]  # 캐릭터 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 가운데
character_y_pos = screen_height - character_height  # 화면 세로의 아바닥

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 1

# 이벤트 루프
running = True  # 게임이 진행중인가
while running:
    dt = clock.tick(120)  # 게임화면의 초당 프레임 수 설정

    for event in pygame.event.get():  # 어떤 이벤트 발생?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 실행시
            running = False

        # if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지
        #     if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
        #         to_x -= 10
        #     elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
        #         to_x += 10
        #     elif event.key == pygame.K_UP:  # 캐릭터를 위로
        #         to_y -= 10
        #     elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
        #         to_y += 10

        # if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         to_x = 0
        #     elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #         to_y = 0

        # character_x_pos += to_x
        # character_y_pos += to_y
        # # 가로 경계값 처리
        # if character_x_pos < 0:
        #     character_x_pos = 0
        # elif character_x_pos > screen_width - character_width:
        #     character_x_pos = screen_width - character_width

        # # 세로 경계값 처리
        # if character_y_pos < 0:
        #     character_y_pos = 0
        # elif character_y_pos > screen_height - character_height:
        #     character_y_pos = screen_height - character_height

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

    # screen.fill((0,0,255)) #배경화면 색으로 채우기 (R,G,B)값
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    pygame.display.update()  # 게임화면 다시 그리기

# pygame 종료
pygame.quit()
