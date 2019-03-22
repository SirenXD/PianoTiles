import ScreenManager
import cv2
import time
import pyautogui


def init():
    #Init some boring stuff
    global manager
    global targetColor
    global firstTileBounds
    global secondTileBounds
    global thirdTileBounds
    global fourthTileBounds
    pyautogui.MINIMUM_DURATION = 0.0
    pyautogui.PAUSE = 0.0
    pyautogui.MAXIMUM_SLEEP = 0.0


    manager = ScreenManager.ScreenManager()
    manager.capture()

    targetColor = [149,244,66, 255]
    firstTileBounds = [85, 10,1,800]
    secondTileBounds = [242,10, 1,800]
    thirdTileBounds = [398,10,1,800]
    fourthTileBounds = [555, 10, 1, 800]
    method()

def startGame():
    startColor = [198,159,54,255]

    data = [manager.checkPart(startColor, firstTileBounds), manager.checkPart(startColor, secondTileBounds),
            manager.checkPart(startColor, thirdTileBounds), manager.checkPart(startColor, fourthTileBounds)]
    for i in range(len(data)):
        if (data[i] is not -1):
            pyautogui.moveTo(data[i][0], data[i][1])
            pyautogui.click()

    time.sleep(.1)

def method():
    while True:
        last_time = time.time()
        manager.capture()

        lowestY = 0
        curCol = 0

        data = [manager.checkPart(targetColor, firstTileBounds), manager.checkPart(targetColor, secondTileBounds),
            manager.checkPart(targetColor, thirdTileBounds), manager.checkPart(targetColor, fourthTileBounds)]

        for i in range(len(data)):
            if (data[i] is not -1):
                if lowestY < data[i][1]:
                    lowestY = data[i][1]
                    curCol = i

        if(data[curCol] is not -1):
            pyautogui.moveTo(data[curCol][0]+635, data[curCol][1]+145)
            pyautogui.click()

        print("fps: {}".format(round(1 / (time.time() - last_time))))

init()