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

meowList=["meowOne.wav","meowTwo.mp3","meowThree.mp3","meowFour.mp3","meowFive.mp3","meowSix.mp3","meowSeven.mp3"]
playbackList=[]
for i in range(0,7):
    playbackList.append(Playback(resource_path(os.path.join("audio", meowList[i]))))
index=2

screen = turtle.Screen()
screen.setup(width=500, height=500)
turtle.hideturtle()
turtle.write("Press g to meow and x to exit.", align="center")
turtle.penup()
turtle.sety(-20)
turtle.pendown()
turtle.write("Use the numbers 1-6 to set the meow sfx.", align="center")
def playSound():
    global index
   # print("playing sound "+str(index))
    playbackList[index].play()
screen.onkeypress(turtle.bye, "x")

def setASingleVariable(i):
    #print(i)
    global index
    index=i

for i in range(1,8):
    #print(i)
    screen.onkeypress(lambda i=i:setASingleVariable(i-1), str(i))

screen.onkeypress(playSound, "g")
screen.listen()
turtle.mainloop()
#print("done\n")
