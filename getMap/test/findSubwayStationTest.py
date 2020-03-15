import cv2 as cv
import numpy as np

def find_all_circles():
    src = cv.imread('./demo4.png', cv.IMREAD_COLOR)
    img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    #img = cv.medianBlur(img, 5)
    cimg = src.copy()

    edged = cv.Canny(img, 30, 150)
    #cv.imshow("edged",edged)
    cv.imshow("img.png", img)
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 15, 0, 5)

    print(circles)


    a, b, c = circles.shape
    print(str(circles))
    for i in range(b):
        cv.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv.LINE_AA)
        cv.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv.LINE_AA)  # draw center of circle
   
    cv.imshow("detected circles", cimg)

    #cv.waitKey(0)


def template_image():
    target = cv.imread("./chengduMap02.png")
    tpl = cv.imread("./1.png")
    #cv.imshow("modul", tpl)
    #cv.imshow("yuan", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(target, tl, br, [0, 0, 0])
        cv.imshow("pipei"+np.str(md), target)

        template_image()

        cv.waitKey(0)
        cv.destroyAllWindows()
 
def judge_gray(pv):
    if(pv[0] == 176 and pv[1] == 176 and pv[2] == 176):
        return True
    return False
 
def access_pixels(image):
    #print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("height : %s width : %s channels : %s"%(height, width, channels))
    #开始一个简单的图像识别，将示例图片中的领结给标记出来
    for i  in range(height):
        for j in range(width):
            pv = image[i, j]
            if not judge_gray(pv):
                image[i, j] = [255, 255, 255]
            else: 
                image[i, j] = [0, 0, 255]
    cv.imwrite("./demo4.png", image)
    cv.imshow("demo3", image)

import glob
import os
#time2 = cv.getTickCount()
#find_all_circles()

#path = "E:/Mini Metro/Map/{name}".format(name = "beijing")
#pic_list = sorted(glob.glob(os.path.join(path, 'cd_*.png')), key = os.path.getmtime)

src = cv.imread("./cd_0_0.png")
access_pixels(src)

#print("time:  %s"%((time2-time1)/cv.getTickFrequency()))
#print("i am a pig!!")
cv.waitKey(0)
cv.destroyAllWindows();