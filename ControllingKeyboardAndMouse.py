#Resolution
import pyautogui
resolution = pyautogui.size()
print(resolution)

#Moving The Mouse
import pyautogui
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)


import pyautogui
for i in range(10):
      pyautogui.moveRel(100, 0, duration=0.25)
      pyautogui.moveRel(0, 100, duration=0.25)
      pyautogui.moveRel(-100, 0, duration=0.25)
      pyautogui.moveRel(0, -100, duration=0.25)

# Get and print the mouse coordinates
import pyautogui
x, y = pyautogui.position()
positionStr = 'x:' + str(x).rjust(4) + 'y:' + str(y).rjust(4)
print(x,y)

#Clicking the Mouse

import pyautogui
import time
pyautogui.click(10, 25)

#Mouse Dragging
import pyautogui
import time
pyautogui.click(10, 25)
import pyautogui, time
time.sleep(5)
pyautogui.click()
distance = 200
while distance > 0:
     pyautogui.dragRel(distance, 0, duration=0.2)   # move right
     distance = distance - 5
     pyautogui.dragRel(0, distance, duration=0.2)   # move down
     pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
     distance = distance - 5
     pyautogui.dragRel(0, -distance, duration=0.2)  # move up