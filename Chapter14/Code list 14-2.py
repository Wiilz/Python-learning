class Ball:
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

#建立一个类的实例
myBall = Ball()

#设置一些属性
myBall.direction = "down"
myBall.color = "red"
myBall.size = "small"

#打印对象属性
print "I just created a ball."
print "My ball is", myBall.size
print "My ball is", myBall.color
print "My ball's direction is",myBall.direction 
print "Now I'm going to bounce the ball"
print

#使用一个方法
myBall.bounce()
print "Now the ball's direction is", myBall.direction
