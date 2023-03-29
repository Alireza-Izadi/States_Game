from turtle import Turtle

class State(Turtle):
    
    def __init__(self, city):
        super().__init__()
        self.ht()
        self.penup()
        self.color("black")
        
    def text(self, city, x, y):
        self.goto(x, y)
        self.write(city)
        
    