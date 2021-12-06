#%% 10-12snownight.py	밤에 눈이 오는 모습 그리기
import pygame, random
 
# 게임 엔진 초기화
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
SIZE = [300, 300] #윈도 크기
SNOW_CNT = 70 #눈의 개수
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("눈 오는 밤")
 
# 눈의 좌표 목록 
snow_list = []
 
# snow_list에 SNOW_CNT 수만큼의 좌표를 저장
for i in range(SNOW_CNT):
    x = random.randrange(0, SIZE[0]) # x 좌표 저장
    y = random.randrange(0, SIZE[1]) # y 좌표 저장
    snow_list.append([x, y]) #목록에 추가

#화면 수정에 사용될 시계 저장 
clock = pygame.time.Clock()
 
# 메인 루프
done = False
while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            done = True   
 
    # 배경색을 검은색으로
    screen.fill(BLACK)
 
    # 눈이 내리는 모습을 그리기 
    for i in range(len(snow_list)):
 
        # 눈 모양의 원을 그리기
        radius = 1
        #radius = random.randint(1, 3)
        pygame.draw.circle(screen, WHITE, snow_list[i], radius)
 
        # 눈 snow_list[i]의 y 좌표를 1 증가시켜 눈이 내리도록 수정
        snow_list[i][1] += 1
        #snow_list[i][1] += random.randint(1, 3)
        # 눈 snow_list[i]의 x 좌표를 (-1, 0, 1) 중의 하나를 선택, 이전에 값에 더하여 대입
        snow_list[i][0] += random.randint(-1, 1)
 
        # snow_list[i]가 윈도 바닥으로 넘어 내려 가면, 즉 보이지 않게 되면  
        if snow_list[i][1] > SIZE[1]: #snow_list[i][1]은 snow_list[i] 눈의 y 좌표
            # y 좌표를 위(음수)로 다시 지정
            snow_list[i][1] = random.randrange(-5, 0)
            # x 좌표도 다시 지정, snow_list[i][0]은 snow_list[i] 눈의 x 좌표
            snow_list[i][0] = random.randrange(0, SIZE[0])
 
    pygame.display.update()
    #초당 수정될 프레임 수 지정, 초당 20 프레임 화면이 수정됨  
    clock.tick(20)
 
pygame.quit()    