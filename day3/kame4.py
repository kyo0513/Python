import turtle
t=turtle.Turtle()
t.shape('turtle')
t.forward(100) # 向いている方向に100移動

"""
t.right(144)  
t.forward(100)
t.right(144)  
t.forward(100)
t.right(144)  
t.forward(100)
t.right(144)  
t.forward(100)
"""

for i in range(4):
    t.right(144)  
    t.forward(100)



t.right(144)
turtle.mainloop()
