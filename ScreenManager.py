import mss
from PIL import Image
import numpy as np


class ScreenManager:
    #Handles taking pictures
    __sct = None
    #The picture
    __currentCap = None

    def __init__(self):
        self.__sct = mss.mss()

    #Takes a picture of Monitor #0 (main display)
    def capture(self):
        monitor = {"top":145, "left":640, "width":635, "height":855}
        self.__currentCap = self.__sct.grab(monitor)

    #Bounds is StartX,StartY,W,H
    def checkPart(self, color, bounds):
        curImg = list(self.getAsNP())
        for j in range(bounds[1]+bounds[3], bounds[1], -1):
            # print(curImg[j][bounds[0]], j)
            if curImg[j][bounds[0]].tolist() == color:
                return [bounds[0], j]

        return -1