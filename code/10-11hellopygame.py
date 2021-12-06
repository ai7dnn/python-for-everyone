#%% 10-11hellopygame.py	pygame 윈도에 Hello, pygame! 표시 
import pygame
 
# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
 
pygame.init()
 
# 윈도 크기 지정
size = [300, 200]
screen = pygame.display.set_mode(size)
#제목인 캡션 지정 
pygame.display.set_caption("Hello, pygame!")
  
# 폰트 생성과 출력할 문자열 지정
font = pygame.font.SysFont('Arial', 20)
outstr = 'Hello, PyGame!' 
 
# 메인 루프
done = False
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
 
    screen.fill(WHITE) 
    #지정된 문자열 글씨를 그린 화면을 반환하여 text에 저장
    text = font.render(outstr, True, BLUE) 
    #글씨가 그려진 화면인 text를 윈도 스크린 위치 [x, y]에 그리기
    screen.blit(text, [100, 80])
 
    pygame.display.update()
 
pygame.quit()
