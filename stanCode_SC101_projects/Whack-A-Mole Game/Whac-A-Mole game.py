"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700

# Constant controls the pause time of the animation
DELAY = 600

score = 0
score_label = GLabel("Score: " + str(score))

# Global variables
# TODO:
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title="whack a mole")


def main():
    score_label.font = "-30"
    window.add(score_label, 0, score_label.height)  # 因為label的原點在label左下角
    onmouseclicked(remove_mole)
    while True:
        img = GImage("bb.png")  # 注意要在same path or 寫出路徑 # 出現的最後一個才算數
        x_random = random.randint(0, window.width-img.width)  # randint（start, end都含）
        y_random = random.randint(0, window.height-img.height)
        window.add(img, x_random, y_random)  # 圖的左上角就是(x_random, y_random0)
        pause(DELAY)  # 要記得加pause，因為while true太快


def remove_mole(event):
    global score  # 如果要變更global var.的本值，需要先呼喊他的名字
    maybe_mole = window.get_object_at(event.x, event.y)
    if maybe_mole is not None and maybe_mole is not score_label:
        window.remove(maybe_mole)
        score += 1
        score_label.text = "Score: " + str(score)


if __name__ == '__main__':
    main()
