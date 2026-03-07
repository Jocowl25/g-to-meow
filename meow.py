import turtle
from just_playback import Playback
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

filename = resource_path(os.path.join("audio", "meow.wav"))

playback = Playback()
playback.load_file(filename)

screen = turtle.Screen()
screen.setup(width=500, height=500)
turtle.write("Press g to meow and x to exit. \n", align="center")
def playSound():
    print("playing sound")
    playback.play()
screen.onkeypress(playSound, "g")
screen.onkeypress(turtle.bye, "x")
screen.listen()
turtle.mainloop()
print("done\n")
