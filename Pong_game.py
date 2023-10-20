from turtle import Turtle , Screen
from time import sleep
from winsound import Beep
initial_angle=37
y_wall=290
X=360          #initial position of paddles horizontal
Y=0
ball_speed=8

#ball class to create a ball object
class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.ballspeed=ball_speed

#scoreboard class to create scoreboard 
class Scoreboard(Turtle):
    def __init__(self,L,R) -> None:
        super().__init__()
        self.color("White")
        self.ht()
        self.pu()
        self.goto(0,240)
        self.write(f"{L}     {R}",font=("Arial",40,"bold"),align="center")


#main game class
class Game:
    def __init__(self) -> None:
        self.screen=Screen()
        self.paddles=[]     #list to store objects of paddles i.e. left and right
        self.x_up=10        #bouncing distance for horizontal direction
        self.y_up=10        #bouncing distance for vertical direction
        self.Lscr=0         #left score
        self.Rscr=0         #right score

        self.screen.tracer(0)                           #for animation
        self.score=Scoreboard(self.Lscr,self.Rscr)      #scoreboard object created
        self.screen.setup(800,600)                  
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.ball_angle=initial_angle                   #starting angle for ball .. not in use
        self.divider()                                  #to create midline of the screen

        self.make_paddle(X,Y)                           #two objects created
        self.make_paddle(-X-10,Y)
        self.screen.update()

        self.ball=Ball()
        self.screen.update()

        self.run_game()
        self.screen.exitonclick()
    
    def run_game(self):
        while True:                 #main loop for the game with every condition
            
            self.score.clear()
            self.score=Scoreboard(self.Lscr,self.Rscr)      
            self.new_ball()
            self.ball_collision()           #condition for ball bouncing with paddles
            self.wall_collision()           #condition for ball bouncing with walls
            self.move_paddle()              #main function for movement of players
            self.ball_move()                #main function for movement of ball

    def make_paddle(self,x,y):
        self.paddle=Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.pu()
        self.paddle.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle.goto(x,y)
        self.paddles.append(self.paddle)
    
    def ball_move(self):
        
        self.screen.update()
        sleep(1-self.ball.ballspeed/10)
        self.new_x=self.ball.xcor()+self.x_up
        self.new_y=self.ball.ycor()+self.y_up
        self.ball.goto(self.new_x,self.new_y)


    def wall_collision(self):
        if self.ball.ycor() >= 280 or self.ball.ycor() <= -280:
            self.ball_bounce()
            Beep(300,60)

    
    def ball_collision(self):
        
        if self.ball.distance(self.paddles[0]) < 50 and self.ball.xcor()>340 or self.ball.distance(self.paddles[1]) < 50 and self.ball.xcor() < -340:
            self.ball_bounce2()
            Beep(600,60)
    
    def new_ball(self):
        
        if self.ball.xcor() >= 400 :
            Beep(600,100)
            self.Lscr+=1
            self.ball.goto(0,0)
            self.ball_bounce2()
        elif self.ball.xcor() <=-400:
            Beep(600,100)
            self.Rscr+=1
            self.ball_bounce2()
            self.ball.goto(0,0)

    def ball_bounce(self):
        self.y_up*=-1
    
    def ball_bounce2(self):
        self.x_up*=-1
        if self.ball.ballspeed<9.6:
            self.ball.ballspeed+=0.3

    def divider(self):
        pen=Turtle()
        pen.ht()
        pen.color("white")
        pen.pensize(3)
        pen.pu()
        pen.goto(0,300)
        pen.setheading(270)
        for _ in range(20):
            pen.pd()
            pen.fd(20)
            pen.pu()
            pen.fd(10)
    
    def move_paddle(self):
        def up():
            new_y=self.paddles[0].ycor()+20
            self.paddles[0].goto(X,new_y)
            self.screen.update()

        def down():
            new_y=self.paddles[0].ycor()-20
            self.paddles[0].goto(X,new_y)
            self.screen.update()

        def up_l():
            new_y=self.paddles[1].ycor()+20
            self.paddles[1].goto(-X-10,new_y)
            self.screen.update()

        def down_l():
            new_y=self.paddles[1].ycor()-20
            self.paddles[1].goto(-X-10,new_y)
            self.screen.update()

        self.screen.listen()
        self.screen.onkey(up,"Up")
        self.screen.onkey(down,"Down")
        self.screen.listen()
        self.screen.onkey(up_l,"w")
        self.screen.onkey(down_l,"s")

game1=Game()        #game object created