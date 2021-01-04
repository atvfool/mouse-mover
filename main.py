import pyautogui, random, time

minX = 0
minY = 0
maxX = 1920
maxY = 1080

while(True):
    try:
        action = random.randint(0, 3)
        if action == 0:
            # going with right click to hopefully not actually change anything
            print("Right click")
            pyautogui.rightClick()
        elif action == 1:
            # move the mouse to a random spot
            xpos = random.randint(minX, maxX)
            ypos = random.randint(minY, maxY)
            print("Moving to " + str(xpos) + "," + str(ypos))
            pyautogui.moveTo(xpos,ypos, 0.5)
        elif action == 2:
            # press escape (shouldn't mess anything up)
            print("Pressing Esc")
            pyautogui.press("esc")
        elif action == 3:
            # change windows with Alt+Tab
            print("Change Windows with Alt+Tab")
            pyautogui.keyDown("alt")
            pyautogui.keyDown("tab")
            pyautogui.keyUp("alt")
            pyautogui.keyUp("tab")

        sleeptime = random.randint(1, 10) 
        print("Sleep for " + str(sleeptime))
        time.sleep(sleeptime)
    except KeyboardInterrupt:
        break
