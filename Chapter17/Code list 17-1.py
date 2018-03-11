import sys, pygame

#定义Ball子类
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location): 
        pygame.sprite.Sprite.__init__(self)         #初始化动画精灵
        self.image = pygame.image.load(image_file)  #向其中加载图像文件
        self.rect = self.image.get_rect()           #得到定义图像边界的矩形
        self.rect.left, self.rect.top = location    #设置球的初始位置

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "beach_ball.png"
balls = []
for row in range(0,3):
    for column in range(0,3):
        location = [column * 180 + 10, row * 180 +10]  #每次循环时都有一个不同的位置
        ball = MyBallClass(img_file, location)         #在这个位置创建一个球
        balls.append(ball)                             #把球收集到一个列表中
for ball in balls:
    screen.blit(ball.image, ball.rect)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
