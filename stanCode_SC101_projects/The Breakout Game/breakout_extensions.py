"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
adding score and game over label.

The aim of the game is to break the bricks of a brick wall by getting the ball to hit/bounce on the bricks.
The score corresponds to the number of bricks being hit.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extensions import BreakoutGraphics
from campy.graphics.gobjects import GLabel

# Constant
FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    total_bricks_num = graphics.bricks_num
    score = graphics.score
    dx = graphics.get_dx()
    dy = graphics.get_dy()

    # Add animation loop here!
    while lives > 0:          # keeping playing
        if graphics.running:  # after clicked, running==True, and ball starts moving
            while True:      # check status every loop if ball needs to change direction or finish game or remove object
                # Ball starts moving.
                graphics.ball.move(dx, dy)

                # the four vertex outside the ball
                left_upper = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                left_lower = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
                right_upper = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
                right_lower = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                            graphics.ball.y + graphics.ball.height)
                # check if the any vertex of ball bumps into object(paddle of bricks)
                if left_upper is not None and left_upper is not graphics.score_label \
                        and left_upper is not graphics.point1 and left_upper is not graphics.point2 \
                        and left_upper is not graphics.point3:
                    if left_upper is graphics.paddle:               # when ball bumps into paddle
                        if dy > 0:
                            dy = -dy
                    else:                                           # when ball bumps into brick
                        dy = -dy
                        graphics.window.remove(left_upper)          # remove bricks from window
                        total_bricks_num -= 1
                        score += 1
                        graphics.score_label.text = "Score: " + str(score)  # update score

                elif left_lower is not None and left_lower is not graphics.score_label \
                        and left_lower is not graphics.point1 and left_lower is not graphics.point2 \
                        and left_lower is not graphics.point3:
                    if left_lower is graphics.paddle:                # when ball bumps into paddle
                        if dy > 0:
                            dy = -dy
                    else:
                        dy = -dy
                        graphics.window.remove(left_lower)           # remove bricks from window
                        total_bricks_num -= 1
                        score += 1
                        graphics.score_label.text = "Score: " + str(score)  # update score
                elif right_upper is not None and right_upper is not graphics.score_label \
                        and right_upper is not graphics.point1 and right_upper is not graphics.point2 \
                        and right_upper is not graphics.point3:
                    if right_upper is graphics.paddle:               # when ball bumps into paddle
                        if dy > 0:
                            dy = -dy
                    else:
                        dy = -dy
                        graphics.window.remove(right_upper)          # remove bricks from window
                        total_bricks_num -= 1
                        score += 1
                        graphics.score_label.text = "Score: " + str(score)  # update score
                elif right_lower is not None and right_lower is not graphics.score_label \
                        and right_lower is not graphics.point1 and right_lower is not graphics.point2 \
                        and right_lower is not graphics.point3:
                    if right_lower is graphics.paddle:               # when ball bumps into paddle
                        if dy > 0:
                            dy = -dy
                    else:
                        dy = -dy
                        graphics.window.remove(right_lower)           # remove bricks from window
                        total_bricks_num -= 1
                        score += 1
                        graphics.score_label.text = "Score: " + str(score)  # update score
                # when ball bumps into window
                if 0 >= graphics.ball.x or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    dx = -dx
                if 0 >= graphics.ball.y:
                    dy = -dy
                if graphics.ball.y >= graphics.window.height:          # when ball fall outside window
                    lives -= 1
                    if lives == 2:
                        graphics.window.remove(graphics.point3)
                    elif lives == 1:
                        graphics.window.remove(graphics.point2)
                    else:
                        graphics.window.remove(graphics.point1)

                    graphics.running = False     # turn off the switch and ball stops running until mouse clicked
                    graphics.window.add(graphics.ball, x=(graphics.window.width / 2 - graphics.ball.width / 2),
                                        y=(graphics.window.height / 2 - graphics.ball.height / 2))
                    break                                               # terminate while loop
                if total_bricks_num == 0:                               # means player wins
                    break
                pause(FRAME_RATE)
        pause(FRAME_RATE)

    # means lives == 0
    graphics.running = False
    graphics.ball.move(0, 0)                                            # the ball won't move anymore

    # create game over loser label
    game_over_label = GLabel("Bye~~Loser!")
    game_over_label.font = "Comic Sans MS-60-bold"
    graphics.window.add(game_over_label, (graphics.window_width - game_over_label.width) / 2,
                        graphics.window_height * 0.7)


if __name__ == '__main__':
    main()
