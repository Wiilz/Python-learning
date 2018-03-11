import sys, pygame
from random import *

#定义Ball子类
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location): 
        pygame.sprite.Sprite.__init__(self)         #初始化动画精灵
        self.image = pygame.image.load(image_file)  #向其中加载图像文件
        self.rect = self.image.get_rect()           #得到定义图像边界的矩形
        self.rect.left, self.rect.top = location    #设置球的初始位置
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
    
def animate(group):
    screen.fill([255,255,255])
    for ball in group:     #从组删除精灵
        group.remove(ball)
        if pygame.sprite.spritecollide(ball, group, False): #精灵与组之间的碰撞
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]

        group.add(ball)   #将球再添回原来的组中
        ball.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    pygame.time.delay(20)

#主程序
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "beach_ball.png"
#img_file = "b_ball_rect.png" 矩形碰撞检测的原画
group = pygame.sprite.Group()  #创建精灵组
#只创建4个球
for row in range(0,2):
    for column in range(0,2):
        location = [column * 180 + 10, row * 180 +10]  #每次循环时都有一个不同的位置
        speed = [choice([-2,2]), choice([-2,2])]
        ball = MyBallClass(img_file, location)         #在这个位置创建一个球
        group.add(ball)                             #把球增加到组

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    animate(group)
pygame.quit()

