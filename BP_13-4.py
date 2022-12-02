from turtle import*

class MyTurtle(Turtle):
    def glow(self,x,y):
        self.fillcolor("red")
turtle = MyTurtle()
turtle.shape("turtle") #tuetle의 모양을 turtle로 해준다
turtle.onclick(turtle.glow)

