#%% Mini Project 6 13-06-pygameballbouncing.py
import pygame 
import random
 
BLACK = (0, 0, 0)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BALL_SIZE = 25
 
class Ball:
    '''공을 표현하는 클래스'''
    def __init__(self):
        #공의 중심 좌표를 임의로 지정 
        self.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
        self.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

        #다음 이동 방향을 설정
        self.change_x = 0
        while self.change_x == 0 or self.change_y == 0:
            self.change_x = random.randint(-4, 4)
            self.change_y = random.randint(-4, 4)

        #공의 색상을 지정 
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        self.color = (r, g, b)
         
#메인 프로그램
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("공의 자동 이동(스페이스바를 누르면 공이 더 생깁니다.)") 
clock = pygame.time.Clock()

#여러 볼의 갖는 리스트에 첫 볼을 저장 
lstballs = []
lstballs.append(Ball())
 
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #스페이스 바를 누르면 새로운 공이 나오도록 
            if event.key == pygame.K_SPACE:
                lstballs.append(Ball())

    for ball in lstballs:
        #볼의 중심 좌표를 이동
        ball.x += ball.change_x
        ball.y += ball.change_y
 
        #윈도 벽에 맞고 바운싱
        #x 좌표가 위 이래를 벗어나면   
        if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
            ball.change_x *= -1 #다음 이동 좌표의 증가 값을 부호 변경 
        #y 좌표가 위 이래를 벗어나면   
        if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
            ball.change_y *= -1 #다음 이동 좌표의 증가 값을 부호 변경 
 
    screen.fill(BLACK)
 
    #모든 볼을 그리기
    for ball in lstballs:
        pygame.draw.circle(screen, ball.color, [ball.x, ball.y], BALL_SIZE)
 
    # 초당 60 프레임으로 그리기
    clock.tick(60) 
    pygame.display.flip()
 
pygame.quit()
