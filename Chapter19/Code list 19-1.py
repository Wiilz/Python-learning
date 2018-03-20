import pygame, sys
#初始化Pygame和mixer
pygame.init()
pygame.mixer.init()

#创建一个Pygame窗口
screen = pygame.display.set_mode([640,480])
#等一秒钟让mixer完成初始化
pygame.time.delay(1000)

#创建声音对象
splat = pygame.mixer.Sound("splat.wav")
splat.play()

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
