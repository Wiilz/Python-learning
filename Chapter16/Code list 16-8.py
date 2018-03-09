import pygame, sys, math

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])   #用白色背景填充窗口
plotPoints = []

for x in range(0, 640):      #从左到右循环(x= 0到639)
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)   #计算每个点的y坐标（垂直坐标）
    plotPoints.append([x,y])    #要连接点的列表
pygame.draw.lines(screen, [0,0,0], False, plotPoints, 2)  
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
