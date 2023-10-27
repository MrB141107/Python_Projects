import turtle

class sketch_book:
    def __init__(self) -> None:
        self.tim=turtle.Turtle()
        self.screen=turtle.Screen()
        color=self.screen.textinput("color","choose the color of pen ")
        size=self.screen.textinput("size","choose the size of pen (in range 1 to 10)")
        self.tim.color(color)
        self.tim.pensize(size)
        self.listen()
        self.screen.mainloop()
    
    def movefd(self):
        self.tim.fd(30)

    def movebk(self):
        self.tim.bk(30)

    def left(self):
        self.tim.left(10)

    def right(self):
        self.tim.right(10)

    def clear(self):
        self.tim.clear()

    def listen(self):
        self.screen.listen()
        self.screen.onkeypress(key="Up",fun=self.movefd)
        self.screen.onkeypress(key="Down",fun=self.movebk)
        self.screen.onkeypress(key="Left",fun=self.left)
        self.screen.onkeypress(key="Right",fun=self.right)
        self.screen.onkeypress(key="c",fun=self.clear)
        self.tim.ondrag(self.tim.goto)

if __name__=="__main__":
    game1=sketch_book()
        