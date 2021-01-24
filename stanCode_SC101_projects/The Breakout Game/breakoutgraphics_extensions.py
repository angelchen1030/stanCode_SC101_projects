"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
The aim of the game is to break the bricks of a brick wall by getting the ball to hit/bounce on the bricks.
The score corresponds to the number of bricks being hit.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).

BALL_RADIUS = 10       # Radius of the ball (in pixels).

PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # create score label
        self.score = 0
        self.score_label = GLabel("Score: " + str(self.score))
        self.score_label.font = "Comic Sans MS-20-bold"
        self.window.add(self.score_label, 0, self.window_height-self.score_label.height)

        # create three hit points
        self.point1 = GOval(ball_radius*2, ball_radius*2, x=self.window_width - ball_radius*3,
                            y=self.window_height-self.window_height*0.06)
        self.point2 = GOval(ball_radius * 2, ball_radius * 2, x=self.window_width - ball_radius*6,
                            y=self.window_height-self.window_height*0.06)
        self.point3 = GOval(ball_radius * 2, ball_radius * 2, x=self.window_width - ball_radius*9,
                            y=self.window_height-self.window_height*0.06)
        self.point1.filled = True
        self.point2.filled = True
        self.point3.filled = True
        self.point1.color = "white"
        self.point2.color = "white"
        self.point3.color = "white"
        self.point1.fill_color = "salmon"
        self.point2.fill_color = "salmon"
        self.point3.fill_color = "salmon"
        self.window.add(self.point1)
        self.window.add(self.point2)
        self.window.add(self.point3)

        # create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2,
                        y=self.window_height-paddle_offset-paddle_height)

        # center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window_width/2-ball_radius),
                          y=(self.window_height/2-ball_radius))
        self.ball.filled = True
        self.window.add(self.ball)

        # default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        self.reset_dx()
        # Initialize our mouse listeners.
        self.running = False
        onmouseclicked(self.start_running)
        onmousemoved(self.reset_paddle_position)

        # Draw bricks.
        for i in range(brick_cols):
            x_position = 0
            x_position += (brick_width + brick_spacing)*i
            for j in range(brick_rows):
                y_position = brick_offset
                y_position += (brick_height + brick_spacing)*j
                self.bricks = GRect(brick_width, brick_height)
                # coloring
                self.bricks.filled = True
                self.bricks.color = "white"
                if j == 0 or j == 1:
                    self.bricks.fill_color = "black"
                elif j == 2 or j == 3:
                    self.bricks.fill_color = "navy"
                elif j == 4 or j == 5:
                    self.bricks.fill_color = "steelblue"
                elif j == 6 or j == 7:
                    self.bricks.fill_color = "skyblue"
                else:
                    self.bricks.fill_color = "lightblue"
                self.window.add(self.bricks, x=x_position, y=y_position)
        self.bricks_num = brick_cols * brick_rows

    def start_running(self, event):
        self.running = True

    def reset_dx(self):
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dx(self):   # makes breakout.py file can get values of dx & dy
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset_paddle_position(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width/2
        if 0 + self.paddle.width/2 > mouse.x:
            self.paddle.x = 0
        if mouse.x > self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
