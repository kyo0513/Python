import turtle
t=turtle.Turtle()
t.shape('turtle')
t.color('blue')
t.forward(100) # 向いている方向に100移動

for i in range(4):
    t.right(144)  
    t.forward(100)

t.right(144)


for i in range(10):
    t.right(108)  
    t.forward(100)



turtle.mainloop()
