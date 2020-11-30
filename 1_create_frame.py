import pygame

pygame.init()  # 초기화(반드시 해야함)

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("make_my_game")  # 게임이름

# 이벤트 루프
running = True  # 게임이 진행중인가
while running:
    for event in pygame.event.get():  # 어떤 이벤트 발생?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 실행시
            running = False

# pygame 종료
pygame.quit()
