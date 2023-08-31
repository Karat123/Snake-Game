from turtle import Turtle
class Snake:
    def __init__(self):
       self.snake_segments = []
       self.create_snake()


    def create_snake(self):
        for snakes in range(3):
            new_snake_segment = Turtle()
            new_snake_segment.shape('square')
            new_snake_segment.color('white')
            new_snake_segment.penup()
            new_snake_segment.goto(x=0 - (20 * snakes), y=0)
            self.snake_segments.append(new_snake_segment)


    def snake_extend(self):
        new_snake_segment = Turtle()
        new_snake_segment.shape('square')
        new_snake_segment.color('white')
        new_snake_segment.penup()
        #new_snake_segment.goto(x=60 - (len(self.snake_segments)), y=0)
        self.snake_segments.append(new_snake_segment)
        self.move_snake()

    def move_snake(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            x_cord = self.snake_segments[segment - 1].xcor()
            y_cord = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(x_cord, y_cord)
        self.snake_segments[0].forward(20)

    def snake_up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)


    def snake_down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)


    def snake_right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)


    def snake_left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)

