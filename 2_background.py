import pygame

pygame.init()  # 초기화(반드시 해야함)

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("make_my_game")  # 게임이름

# 배경 이미지 불러오기
background = pygame.image.load(
    "C:\\Users\\littl\\OneDrive\\바탕 화면\\python\\pygame_basic\\background.png")

# 이벤트 루프
running = True  # 게임이 진행중인가
while running:
    for event in pygame.event.get():  # 어떤 이벤트 발생?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 실행시
            running = False

    # screen.fill((0,0,255)) #배경화면 색으로 채우기 (R,G,B)값
    screen.blit(background, (0, 0))  # 배경 그리기
    pygame.display.update()  # 게임화면 다시 그리기

# pygame 종료
pygame.quit()
