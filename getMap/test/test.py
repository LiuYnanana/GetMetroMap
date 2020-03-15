import os
import glob
import cv2 as cv
import numpy as np


def judge_gray(pv):
    if(pv[0] == 252 and pv[1] == 220 and pv[2] == 174):
        return True
    return False

def access_pixels(image):
    #print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("height : %s width : %s channels : %s"%(height, width, channels))
    #开始一个简单的图像识别，将示例图片中的领结给标记出来
    cnt = 0
    for i  in range(height):
        for j in range(width):
            pv = image[i, j]
            #if(pv[0] == 174):
            #print(pv)

            if not judge_gray(pv):
                image[i, j] = [255, 255, 255]
            else:
                cnt += 1

    print(cnt)
            
    cv.imwrite("./demo4.png", image)
    cv.imshow("demo3", image)

img = cv.imread("E:/Mini Metro/Map/beijing/beijing.png")
#cv.imshow("aa", img)
access_pixels(img)
cv.waitKey(0)
cv.destroyAllWindows();