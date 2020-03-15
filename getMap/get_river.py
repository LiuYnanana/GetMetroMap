import os
import glob
import cv2 as cv
import numpy as np
import com_tool

class River(object):
    def __init__(self, place, picture_path, river_path):
        self.place = place
        self.picture_path = picture_path
        self.river_path = river_path
        self.river_point = []

    def judge_river(self, pv):
        if(pv[0] == 252 and pv[1] == 220 and pv[2] == 174):
            return True
        return False

    def access_pixels_river(self, image):
        height = image.shape[0]
        width = image.shape[1]
        channels = image.shape[2]
        print("height : %s width : %s channels : %s" % (height, width, channels))
        for i  in range(height):
            for j in range(width):
                pv = image[i, j]

                if not self.judge_river(pv):
                    image[i, j] = [255, 255, 255]
                else:
                    self.river_point.append((i, j))

        cv.imwrite(self.river_path + "/river_{name}.png".format(name = self.place), image)

    def get_river(self):
        com_tool.make_dir(self.river_path)
        img = cv.imread(self.picture_path)
        self.access_pixels_river(img)

#beijing = River("Beijing", "E:/MiniMetro/Picture/Beijing/Map/Beijing.png", "E:/MiniMetro/Picture/Beijing/River")
#beijing.get_river()