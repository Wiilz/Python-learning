> 1. 程序可以响应哪两种事件？

程序可以响应的两种事件分别是键盘事件和鼠标事件。


> 2. 处理事件的代码叫什么？

处理事件的代码称为事件处理器。


> 3. Pygame 检测按键时使用的事件类型名是什么？

 ygame 使用 KEYDOWN 事件来检测按键是否按下。
 

> 4. MOUSEMOVE 事件的哪个属性指出了鼠标位于窗口的哪个位置？

 os 属性会指出事件发生时鼠标所在的位置。
 

> 5. 如何找出 Pygame 中下一个可用的事件编号（例如，如果你想添加一个用户事
件）？

为用户事件得到下一个可用的事件编号，可以使用 pygame.NUMEVENTS。


> 6. 如何创建一个定时器在 Pygame 中生成定时器事件？

创建一个定时器，可以使用 pygame.time.set_timer()。


> 7. 在 Pygame 窗口中显示文本时要使用什么对象

在 Pygame 窗口中显示文本，可以使用 font 对象。


> 8. 要让文本出现在一个 Pygame 窗口中，需要哪 3 个步骤？
- 创建一个字体对象； 
- 渲染文本，创建一个表面； 
- 把这个表面块移到显示表面。 