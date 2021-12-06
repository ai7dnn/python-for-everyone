#%% 10-10firstpygame.py	첫 pygame 윈도 
import pygame
 
# 색상 정의
WHITE = (255, 255, 255)
# 윈도 크기 정의
size = (300, 200)
 
# 윈도 초기화
pygame.init()
 
# 화면 크기 지정해 스크린을 생성 
screen = pygame.display.set_mode(size)
#제목인 캡션 지정 
pygame.display.set_caption('첫 파이게임 윈도!')

# 윈도 종료 플래그로 사용되는 변수 초기값 지정
done = False
# 메인 루프
while not done:
    for event in pygame.event.get():  # 여러 이벤트를 받아 처리
        if event.type == pygame.QUIT:  # 윈도 종료 버튼을 누르면 
            done = True  # 프로그램 종료하기 위해 True 지정 
 
    screen.fill(WHITE) #스크린 색상을 흰색으로 지정
    pygame.display.update() # 화면의 필요한 부분만을 수정 
    #pygame.display.flip() # 화면을 전체 수정 

#메인 루프를 빠져나오면 프로그램 종료
pygame.quit()