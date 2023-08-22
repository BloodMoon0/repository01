import turtle as tt

tt.penup()
tt.goto(-300,300)
tt.pendown()

for i in range(3):
    tt.forward(100)
    tt.left(120)

tt.penup()
tt.goto(300,300)
tt.pendown()

for i in range(4):
    tt.forward(100)
    tt.left(90)
    
tt.penup()
tt.goto(-300,-300)
tt.pendown()

for i in range(5):
    tt.forward(100)
    tt.left(72)
    
tt.penup()
tt.goto(300,-300)
tt.pendown()

for i in range(6):
    tt.forward(100)
    tt.left(60)

tt.penup()
tt.goto(0,0)
tt.pendown()
tt.speed(5)

for i in range(18):
    tt.circle(50)
    tt.left(20)